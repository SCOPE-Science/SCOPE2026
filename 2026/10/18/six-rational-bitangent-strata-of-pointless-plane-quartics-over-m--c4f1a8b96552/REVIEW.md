# Independent mathematical audit

## correctness

PASS

For any smooth plane quartic C/F5, a rational line L is a rational bitangent (counting hyperflex degenerations by even divisor) exactly when the binary quartic F|L is a nonzero scalar times the square of a homogeneous binary quadratic over F5. There are 31 rational lines in PG(2,5). The input 31 plane quartic equations were checked entry-by-entry against the original source repository blob 684ea266a0a862882fb8412572efa652889be49b in RationalPoint/excessive's AllGenus3.magma: all 31 expressions match exactly, with no missing/altered entries. Independent SymPy modular polynomial restrictions enumerate all 31 lines on each of all 31 curves, compare normalized coefficient 5-tuples with all 31 projective quadratic-square coefficient signatures, producing 961 fully checked decisions. The exact bitangent numbers in source order are 0,1,1,2,1,2,1,1,2,1,0,2,2,2,2,1,6,1,1,1,1,1,4,2,4,1,1,4,4,0,16. Therefore six distinct realized counts {0,1,2,4,6,16} with frequencies (3,14,8,4,1,1); the unique 16 class is the Fermat x^4+y^4+z^4, with lines (1,b,c) for b,c nonzero. The Faber–Grantham–Howe 31-class input exhaustivity is a named dependency, not newly proved here, and the bitangent scan is exhaustive conditional on it.

## originality

PASS

Faber–Grantham–Howe arXiv:2207.14307v2 already give complete isomorphism classes of 31 pointless smooth genus-three curves over F5, and the source input is literally their public code. This assessment never treats the base curve census as a new result. The original paper's relevant §8 curve enumeration and companion original code include equations and zeta data but do not tabulate rational bitangents, and text search found no bitangent theorem. The six-value rational bitangent spectrum and extremal optimizer within that natural exhaustive catalogue is additional contact geometry. Classical Fermat-quartic automorphisms may separately imply its 16 bitangents; novelty of the individual 16 count is lower confidence, but the full six-stratum distribution is not a known-table recomputation in inspected sources.

## value

PASS

An exact arithmetic incidence invariant evaluated on a natural complete moduli census, with realized spectrum, multiplicities, and distinguished maximum, is a meaningful finite-field classification. Rational bitangents relate to plane quartic contact geometry and odd theta characteristics. This has a clear invariant motivation beyond executing a numerical loop, though novelty depends on crediting the previously complete 31-class input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
