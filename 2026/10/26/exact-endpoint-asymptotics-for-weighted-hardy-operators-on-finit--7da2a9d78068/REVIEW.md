# Independent mathematical audit

## correctness

PASS

Take total q-mass Q=∫Gamma uv>0. Subdivide finitely many edges into N pieces whose q-masses are Q/N+O(N⁻²), with length O(1/N). The map Gf(x)=∫_[o,x]u f has root value zero, hence nodal interpolation on the N-edge subdivision has rank<=N and uniform error <=(max_I sup_I(u) sup_I(v)|I|)/2=(1+o(1))Q/(2N), giving a_(N+1) upper. For each local interval choose f_j=+1 on the first half of its u-mass and −1 on the second, zero elsewhere. Each integrated image has support only on its interval, and has v-weighted peak at least (1−o(1))Q/(2N). On the N-dimensional span of these inputs any rank<N approximation has a normalized nonzero kernel vector, and disjoint tent outputs imply a_N >=(1−o(1))Q/(2N). The shifted upper bound and lower bound prove the exact limit; finite edges and positive uniform-continuity assumptions are used explicitly. I independently checked weighted edge subdivision and disjoint tent peak numerically (N=32 giving scaled minimum 0.499886...), but this is not the infinite proof.

## originality

PASS

PASS qualified best-of-knowledge with material access risk. Evans–Harris–Lang 2001 proves the exact limit for 1<p<∞; Section 5.2 provides endpoint estimates but the inspected statements do not explicitly give this finite-tree equality. Their 1998 endpoint interval paper is especially close and may contain the interval base case; full text inaccessible despite publisher licensing, and authorized institutional retrieval was blocked by safety controls. This access limit alone is not a scientific FAIL.

## value

PASS

The exact endpoint approximation-number coefficient of the natural rooted Hardy integration operator on finite branched metric trees is a meaningful canonical asymptotic invariant. The universal one-half coefficient independent of branch topology distinguishes the L∞ endpoint from the previously quantified 1<p<∞ range; a finite tree is natural, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
