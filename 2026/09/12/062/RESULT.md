# Face-size multisets of minimum-genus orientable embeddings of K(4,9)

For K(4,9), V=13 and E=36. Ringel's orientable genus formula gives

g = ceil((4-2)(9-2)/4) = 4.

Euler's formula then forces F=17 in every minimum-genus cellular embedding. Because K(4,9) is simple and bipartite, every facial boundary has even length at least 4. Since the sum of all face lengths is 2E=72,

sum_f (|f|-4) = 72 - 4·17 = 4.

Every summand is a nonnegative even integer. Therefore the only possible face-size multisets are

- {4^15,6^2}, and
- {4^16,8}.

Both occur. The following explicit rotation systems use A={0,1,2,3} and B={4,...,12}; face tracing uses the successor of the incoming neighbour.

## Witness A: {4^15,6^2}

A-side rotations:
0:(10,7,11,9,6,5,4,8,12)
1:(7,5,6,10,4,9,11,12,8)
2:(6,12,9,4,5,11,8,7,10)
3:(10,12,6,9,11,5,7,8,4)

B-side rotations:
4:(1,3,0,2), 5:(1,3,2,0), 6:(1,0,3,2), 7:(1,0,2,3), 8:(0,3,2,1),
9:(0,1,2,3), 10:(0,3,1,2), 11:(0,2,3,1), 12:(0,1,2,3).

Independent tracing gives 17 faces with lengths fifteen 4s and two 6s.

## Witness B: {4^16,8}

A-side rotations:
0:(10,12,6,11,4,8,9,7,5)
1:(10,7,6,12,9,8,4,11,5)
2:(11,6,4,8,10,5,7,9,12)
3:(8,4,6,7,9,5,11,12,10)

B-side rotations:
4:(3,0,1,2), 5:(1,3,0,2), 6:(3,2,0,1), 7:(3,1,2,0), 8:(0,3,2,1),
9:(1,2,3,0), 10:(3,0,1,2), 11:(2,3,1,0), 12:(1,0,3,2).

Independent tracing gives 17 faces with lengths sixteen 4s and one 8.

Thus these two and only these two face-size multisets occur at minimum orientable genus.

## Reproducibility and limitations

The 2026-09-29 audit reconstructed the face tracer directly from the printed rotations and recovered the stated multisets. The previously referenced `output/artifacts/verify.py` and `output/artifacts/witnesses.json` are not present in the audited repository tree and are not claimed as evidence.

## References

- Grannell and Knor, *An enumeration of minimum genus orientable embeddings of some complete bipartite graphs* (2010), for the standard genus/rotation-system framework and enumerations up to part sizes 7.
- Sun, *Face distributions of embeddings of complete graphs*, arXiv:1708.02092, for related face-distribution questions in the complete-graph family.
