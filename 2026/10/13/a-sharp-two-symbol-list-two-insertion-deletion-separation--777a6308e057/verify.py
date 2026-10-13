"""Independent finite replay for one-edit, list-two, two-symbol codes."""
from itertools import product

def compatible(word, received):
    if len(received) == 1:
        return received[0] in word
    assert len(received) == 3
    return word in (received[:2], (received[0],received[2]), received[1:])

def valid(words, q, received_length):
    for received in product(range(q), repeat=received_length):
        if sum(compatible(word,received) for word in words)>2:
            return False
    return True

def exact_capacity(q, received_length):
    universe=list(product(range(q),repeat=2))
    best=0
    for mask in range(1<<len(universe)):
        size=mask.bit_count()
        if size<=best:continue
        words=[universe[i] for i in range(len(universe)) if mask>>i&1]
        if valid(words,q,received_length):best=size
    return best

def deletion_witness(q):
    return [(i,i) for i in range(q)]+[(2*i,2*i+1) for i in range(q//2)]

def insertion_witness(q):
    return [(i,j) for i in range(q//2) for j in range(q//2,q)]+[(j,i) for i in range(q//2) for j in range(q//2,q)]

assert [(exact_capacity(q,1),exact_capacity(q,3)) for q in (2,3)]==[(3,3),(4,6)]
assert valid([(0,0),(1,1),(2,2),(0,1),(1,2),(2,0)],3,3)
print('EXHAUSTIVE q=2: deletion=3, insertion=3; q=3: deletion=4, insertion=6')
for q in range(2,25):
    assert len(deletion_witness(q))==3*q//2
    assert valid(deletion_witness(q),q,1),(q,'deletion')
    assert len(insertion_witness(q))==2*(q//2)*(q-q//2)
    assert valid(insertion_witness(q),q,3),(q,'insertion')
print('ALL_CONSTRUCTIONS_OK q=2..24')
print('VERIFY_OK')
