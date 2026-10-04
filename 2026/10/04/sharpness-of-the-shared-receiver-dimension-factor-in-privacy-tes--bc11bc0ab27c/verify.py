import numpy as np


def decoder_preimages(M, d, which):
    if which == 1:
        inputs = [(x, c) for x in range(M) for c in range(d)]
    else:
        inputs = [(c, y) for c in range(d) for y in range(M)]
    outputs = [(k, t) for k in range(M) for t in range(d)]
    mapping = {}
    used_in = set()
    used_out = set()
    r = min(M, d)

    if which == 1:
        for j in range(r):
            inp = (0, j)
            out = (j, 0)
            mapping[inp] = out
            used_in.add(inp)
            used_out.add(out)
        if d < M:
            candidates = [z for z in inputs if z[0] != 0 and z not in used_in]
            assert len(candidates) >= M - d
            for j, inp in zip(range(d, M), candidates):
                out = (j, 0)
                mapping[inp] = out
                used_in.add(inp)
                used_out.add(out)
    else:
        for j in range(r):
            inp = (j, 0)
            out = (j, 0)
            mapping[inp] = out
            used_in.add(inp)
            used_out.add(out)

    remaining_in = [z for z in inputs if z not in used_in]
    remaining_out = [z for z in outputs if z not in used_out]
    assert len(remaining_in) == len(remaining_out)
    for inp, out in zip(remaining_in, remaining_out):
        mapping[inp] = out

    in_index = {z: i for i, z in enumerate(inputs)}
    out_index = {z: i for i, z in enumerate(outputs)}
    preimage = [None] * (M * d)
    for inp, out in mapping.items():
        preimage[out_index[out]] = in_index[inp]
    assert all(z is not None for z in preimage)
    return preimage


def check_case(M, d):
    pre1 = decoder_preimages(M, d, 1)
    pre2 = decoder_preimages(M, d, 2)
    total_dim = M * M * d * M

    def index(k, x, c, y):
        return ((k * M + x) * d + c) * M + y

    cols_p = []
    for t in range(d):
        for y in range(M):
            v = np.zeros(total_dim, dtype=complex)
            for k in range(M):
                inp = pre1[k * d + t]
                x, c = divmod(inp, d)
                v[index(k, x, c, y)] = 1 / np.sqrt(M)
            cols_p.append(v)

    cols_q = []
    for t in range(d):
        for x in range(M):
            v = np.zeros(total_dim, dtype=complex)
            for k in range(M):
                inp = pre2[k * d + t]
                c, y = divmod(inp, M)
                v[index(k, x, c, y)] = 1 / np.sqrt(M)
            cols_q.append(v)

    vp = np.stack(cols_p, axis=1)
    vq = np.stack(cols_q, axis=1)
    identity = np.eye(M * d)
    assert np.allclose(vp.conj().T @ vp, identity, atol=1e-12)
    assert np.allclose(vq.conj().T @ vq, identity, atol=1e-12)

    target = min(1.0, d / M)
    designated = abs(np.vdot(vp[:, 0], vq[:, 0]))
    overlap_norm = np.linalg.svd(vp.conj().T @ vq, compute_uv=False)[0]
    assert abs(designated - target) < 1e-12
    assert abs(overlap_norm - target) < 1e-12


for case in [(2, 1), (5, 2), (6, 3), (4, 4), (3, 5), (2, 5)]:
    check_case(*case)

print('VERIFY_OK')
