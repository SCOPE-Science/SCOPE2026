"""Exact bitset boundary-rank verification for two seven-vertex graph complexes.

Only Python standard library is required. All calculations are over F_2.
"""
from itertools import combinations


def three_matchings(vertices):
    if not vertices:
        yield ()
    else:
        a = vertices[0]
        for j in range(1, len(vertices)):
            for rest in three_matchings(vertices[1:j] + vertices[j+1:]):
                yield ((a, vertices[j]),) + rest


def faces(graph_edges):
    edge_index = {edge: i for i, edge in enumerate(graph_edges)}
    forbidden = []
    for six in combinations(range(7), 6):
        for matching in three_matchings(six):
            if all(e in edge_index for e in matching):
                forbidden.append(sum(1 << edge_index[e] for e in matching))
    assert len(set(forbidden)) == len(forbidden)
    grouped = {k: [] for k in (4, 5, 6, 7)}
    for face in range(1 << len(graph_edges)):
        k = face.bit_count()
        if k in grouped and all(face & bad != bad for bad in forbidden):
            grouped[k].append(face)
    return grouped, len(forbidden)


def boundary(face, row_index):
    result = 0
    pending = face
    while pending:
        bit = pending & -pending
        pending -= bit
        result ^= 1 << row_index[face ^ bit]
    return result


def rank_of_boundaries(source_faces, target_faces):
    row_index = {face: i for i, face in enumerate(target_faces)}
    pivots = {}
    for face in source_faces:
        value = boundary(face, row_index)
        while value:
            high = value.bit_length() - 1
            if high in pivots:
                value ^= pivots[high]
            else:
                pivots[high] = value
                break
    return len(pivots)


def check_one(name, edges, expected):
    by, forbidden_count = faces(edges)
    assert forbidden_count == expected['matchings']
    counts = tuple(len(by[i]) for i in (4, 5, 6, 7))
    assert counts == expected['counts'], (name, counts)
    # Two consecutive boundary ranks determine H_4 and H_5.
    rank_d4 = rank_of_boundaries(by[5], by[4])
    rank_d5 = rank_of_boundaries(by[6], by[5])
    rank_d6 = rank_of_boundaries(by[7], by[6])
    ranks = (rank_d4, rank_d5, rank_d6)
    assert ranks == expected['ranks'], (name, ranks)
    # Independently check all d_4 d_5 = d_5 d_6 = 0 identities.
    idx_3 = {face:i for i,face in enumerate(by[4])}
    idx_4 = {face:i for i,face in enumerate(by[5])}
    idx_5 = {face:i for i,face in enumerate(by[6])}
    for face in by[6]:
        chain = boundary(face, idx_4)
        twice = 0
        while chain:
            b = chain & -chain
            chain -= b
            twice ^= boundary(by[5][b.bit_length()-1], idx_3)
        assert twice == 0
    for face in by[7]:
        chain = boundary(face, idx_5)
        twice = 0
        while chain:
            b = chain & -chain
            chain -= b
            twice ^= boundary(by[6][b.bit_length()-1], idx_4)
        assert twice == 0
    h4 = len(by[5]) - rank_d4 - rank_d5
    h5 = len(by[6]) - rank_d5 - rank_d6
    assert (h4, h5) == expected['homology'], (name,h4,h5)
    print(name, 'edge_count=', len(edges), 'faces=', counts,
          'boundary_ranks=', ranks, 'H4_H5=', (h4,h5), 'boundary_square_zero=YES')


def main():
    complete_six = list(combinations(range(6),2))
    graph = sorted([e for e in complete_six if e != (0,1)] + [(0,6),(1,6)])
    completed = sorted(graph + [(0,1)])
    assert len(graph) == 16 and len(completed) == 17
    check_one('subdivided_K6_edge', graph, {
        'matchings': 42,
        'counts': (1361,2188,2103,1162),
        'ranks': (948,1236,862),
        'homology': (4,5),
    })
    check_one('edge_filled', completed, {
        'matchings': 45,
        'counts': (1843,3366,3805,2580),
        'ranks': (1328,2038,1758),
        'homology': (0,9),
    })
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
