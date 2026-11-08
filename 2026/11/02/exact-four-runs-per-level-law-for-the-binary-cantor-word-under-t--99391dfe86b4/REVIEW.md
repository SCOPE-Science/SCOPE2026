# Independent mathematical audit

## correctness

PASS

For C_0=1, C_{k+1}=mu(C_k) with mu(1)=101 and mu(0)=000, positions of ones have base-three digits 0/2, giving cyclic zero gaps g_j=3^{nu_2(j+1)} and terminal g_{2^k-1}=0. Among rotations with t exact leading zeros, only t=3^a have preceding-letter 1; lex comparison of subsequent gap sequences yields block 1^{H-1}0^{H-1}1 for H=2^{k-a-1}. Non-power groups are all-zero. One-initial group is 0^A 1 0^B with A,B>0 for k>=2. Thus exactly 2k 1-runs and 2k 0-runs, r(BWT(C_k))=4k (k>=2), with k0=1, k1=2. Fresh literal cyclic rotation sort n=3^k, k=0..5 confirmed exact numbers and blocks; infinite proof uses the gap recursion.

## originality

PASS

Frosini et al already show logarithmic BWT run asymptotics for growing nonprimitive binary morphisms. The exact coefficient, exceptional initial cases and full ordered block structure for the Cantor morphism remain additional conclusions; novelty is not claimed for logarithmic order itself.

## value

PASS

Determining a precise infinite-family BWT compression invariant of a canonical fractal morphic word is mathematically natural. Exact 4k and the block decomposition enable exact index-run counts beyond a coarse Theta(log n) bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
