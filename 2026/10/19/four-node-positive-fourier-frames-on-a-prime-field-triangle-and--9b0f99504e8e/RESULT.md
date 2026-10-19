# Four-node positive Fourier frames on a prime-field triangle and a sharp rational-weight gap

## Finding
Let \(p\ge5\) be prime, let \(G=\mathbb F_p^2\), and consider the noncollinear spatial triangle \(A=\{(0,0),(1,0),(0,1)\}\). Write \(\zeta=\exp(2\pi i/p)\). The restriction to \(A\) of the character at frequency \(b=(s,t)\in G\) is \(v_b=(1,\zeta^s,\zeta^t)^T\). A positive Fourier design is a set of distinct \(b\), with strictly positive real weights \(w_b\), for which \(\sum_b w_bv_bv_b^*=I_3\).

**Theorem.** For every prime \(p\ge5\):

1. The minimum number of nodes in a positive Fourier design is exactly **four**. In particular, put \(a=(p-1)/2\), \(h=\cos(\pi/p)\), and
   \[
   B=\{(0,0),(a,0),(0,a),(-a,-a)\},\qquad
   w_{(0,0)}=\frac{2h-1}{2(1+h)},\quad
   w_b=\frac1{2(1+h)}\ (b\ne(0,0)).
   \]
   This is a positive four-node design. All its frequency translates are designs.
2. If all the weights are required to be **rational**, the minimum is exactly **\(p\)**, an unbounded multiplicative penalty \(p/4\) compared with unrestricted positive real weights. The \(p\) nodes \(B=\{(t,2t):t\in\mathbb F_p\}\), each of weight \(1/p\), attain this bound.
3. Every rational-weight design with precisely \(p\) nodes is, after indexing its nodes by first frequency coordinate, of the form
   \[
   B=\{(t,f(t)):t\in\mathbb F_p\},\qquad w_b=1/p,
   \]
   where both \(f\) and \(t\mapsto t-f(t)\) are permutations of \(\mathbb F_p\). Conversely every such choice gives a design. Thus rational-optimal designs are parametrized by complete mappings of the additive group.
4. More generally, each integer \(a\) with \(p/3<a<2p/3\) gives a four-node design on \(\{(0,0),(a,0),(0,a),(-a,-a)\}\), assigning weights \(-(1+2c)/(2(1-c))\) at the origin and \(1/(2(1-c))\) at the other nodes, where \(c=\cos(2\pi a/p)\). Translation gives at least \(p^2\lfloor(p+1)/3\rfloor\) distinct positive four-node designs. This count is a lower bound, not an enumeration of all optimizers.

The exhibited canonical four-node weights approach \(1/4\) as \(p\to\infty\); their exact disparity is \((1-h)/(1+h)=\tan^2(\pi/(2p))\). This last formula is a property of the exhibited design, not a claimed global optimum.

## Assumptions and scope
All primes satisfy \(p\ge5\). Frequencies are distinct points of \(\mathbb F_p^2\). The spatial support is exactly the displayed noncollinear three-point set, whose affine translates and invertible linear images give equivalent designs. Real weights are strictly positive and normalized to sum to one. The rational-weight condition is exact membership in \(\mathbb Q\), not a numerical approximation. No statement is made for composite moduli or for arbitrary spatial sets.

For the unnormalized restricted Fourier column \(v_b\), its norm squared is three. The frame normalization used here is precisely \(\sum_bw_bv_bv_b^*=I_3\); no additional scaling by three is hidden.

## Proof
**Moment characterization.** The diagonal of every rank-one operator \(v_bv_b^*\) consists of ones. The three independent off-diagonal entries of the weighted sum are, up to complex conjugation,
\[
\sum_bw_b\zeta^s,\quad\sum_bw_b\zeta^t,\quad\sum_bw_b\zeta^{s-t}.
\]
Thus the exact Parseval condition is \(\sum_bw_b=1\) together with the vanishing of these three complex moments.

**Four real-positive nodes suffice.** Choose an integer \(a\) strictly between \(p/3\) and \(2p/3\). Then \(c=\cos(2\pi a/p)<-1/2\). For the four prescribed nodes, each of the three moment sums is the same real quantity \(w_0+w_*(1+2c)\). The assigned weights are strictly positive; furthermore \(w_0+3w_*=1\) and \(w_0+w_*(1+2c)=0\), by direct substitution. For \(a=(p-1)/2\) one has \(c=-\cos(\pi/p)=-h\), giving the displayed formula. Frequency translation only multiplies each moment by a unit-modulus scalar and therefore preserves its vanishing.

**Three nodes are impossible.** At least three columns are necessary for rank three. If precisely three columns formed a Parseval frame, the square weighted synthesis matrix would be unitary. All three columns would have squared norm one, forcing each \(w_b=1/3\). The first off-diagonal moment would be a sum of three \(p\)-th roots of unity equal to zero. Such a sum does not exist for \(p\ge5\): the polynomial \(P(X)\in\mathbb Z[X]\) recording its three nonnegative coefficients has degree at most \(p-1\), satisfies \(P(\zeta)=0\), and must equal a rational multiple of the irreducible cyclotomic polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). Since its coefficient sum is three and the coefficient sum of \(\Phi_p\) is \(p\), this is impossible. The rank argument excludes one or two nodes.

**Rational minimum and complete \(p\)-node characterization.** If \(w_b\in\mathbb Q_{>0}\), set \(m_s=\sum_{b:\operatorname{first}(b)=s}w_b\). Then \(\sum_sm_s\zeta^s=0\). The rational polynomial \(\sum_sm_sX^s\) is a multiple of \(\Phi_p\), whence all \(m_s\) are equal; normalization gives \(m_s=1/p\) for every \(s\). There must consequently be at least \(p\) distinct nodes. If exactly \(p\) nodes occur, every first coordinate occurs once and its node has weight \(1/p\). Repeating the cyclotomic argument for the second-coordinate moment and the difference-coordinate moment forces both \(f\) and \(t\mapsto t-f(t)\) to be permutations. Conversely these three permutations yield all three vanishing moments. The example \(f(t)=2t\) works because multiplication by \(2\) and by \(-1\) permutes \(\mathbb F_p\).

**Count of exhibited four-node designs.** The interval \(p/3<a<2p/3\) contains exactly \(\lfloor(p+1)/3\rfloor\) integers. For odd primes \(p\ge5\), the central weight differs from the other three weights, and the three satellites are pairwise distinct. Their offsets consist of one unique satellite with second offset zero, one with first offset zero, and one with both offsets nonzero. Consequently the central frequency and \(a\) are recoverable from the weighted design. Its \(p^2\) translates and the allowed values of \(a\) therefore count distinctly. Finally the canonical disparity follows from the half-angle identity \((1-\cos x)/(1+\cos x)=\tan^2(x/2)\).

## Verification
The supplied standalone Python verifier constructs both explicit Gram operators from their complex-valued Fourier columns for the primes \(5,7,11,13,17,31,101\). All fourteen numerical frame tests passed; the greatest entrywise discrepancy from the identity was \(6.66\times10^{-16}\). Positivity, four-node distinctness, and the canonical weight-disparity identity were also checked. These numerical checks support the explicit formulas but do not prove their validity for all primes. The infinite-family conclusion follows from the foregoing algebra and cyclotomic irreducibility.

Run the reproducibility check using `python verify.py`. It requires only the Python standard library. Recorded output is in `verification_output.txt`.

## Relationship to prior work
The classical theory of finite harmonic frames studies restrictions of finite-group characters. Marshall and Waldron's paper on counting harmonic frames treats unweighted harmonic-frame equivalence and counts. Ferguson, Mayeli, and Sothanaphan study Riesz bases of exponentials for finite abelian groups. These structural settings motivate the present positive-node question, but neither inspected work gives a four-node strictly positive sampling design on the prime-field triangle together with a rational-weight lower bound and complete-mapping classification.

Related published results on three **consecutive cyclic** spatial sites and on the **four-point affine simplex** concern different spatial configurations and do not imply the stated three-point prime-field triangle theorem. The new assertion is the combination of the sharp real-positive minimum, the sharp rational minimum, and all rational-optimal designs, not the underlying cyclotomic polynomial identity or the general definition of a tight frame.

## Limitations
The proof does not classify all real-positive four-node designs, and the displayed lower count is not an exact total. The rational distinction has no uniform numerical separation from real designs: rational weights approximating the four-node weights may make arbitrarily small frame errors, but they cannot yield **exact** four-node Parseval identities. No lower stability bounds under perturbed frequencies or weights are claimed. A genuinely equivalent older quadrature/cubature formulation would limit originality; a literature search alone does not establish uniqueness in the literature.

## References
- S. Marshall and S. Waldron, *On the number of harmonic frames*, arXiv:1611.07121, first public version 2016-11-22. https://arxiv.org/abs/1611.07121
- S. Ferguson, A. Mayeli and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, first public version 2019-04-09. https://arxiv.org/abs/1904.04487
- Classical cyclotomic irreducibility for prime \(p\): \(\Phi_p(X)=1+X+\cdots+X^{p-1}\).
