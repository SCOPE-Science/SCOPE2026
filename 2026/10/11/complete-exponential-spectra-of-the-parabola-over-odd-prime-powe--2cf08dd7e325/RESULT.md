# Complete exponential spectra of the parabola over odd prime-power rings

## Finding

Let \(p\) be any odd prime, let \(k\ge1\), and put \(R=\mathbb Z/p^k\mathbb Z\), \(q=p^k\). For the finite parabola
\[
E=\{(t,t^2):t\in R\}\subset R^2,
\]
consider additive characters restricted to \(E\), normalized in \(\ell^2(E)\):
\[
\phi_{a,b}(t)=q^{-1/2}\exp\!\left(\frac{2\pi i}{q}(at+bt^2)\right),\qquad(a,b)\in R^2.
\]
**Classification.** A subset \(\Lambda\subset R^2\) of cardinality \(q\) is an exponential spectrum (the \(\phi_{a,b}\) indexed by \(\Lambda\) form an orthonormal basis) precisely when
\[
\Lambda=\{(a,b(a)):a\in R\}
\quad\text{and}\quad
\nu_p\bigl(b(a)-b(a')\bigr)>\nu_p(a-a')\quad(a\ne a').
\]
Here \(\nu_p(x)\) is the divisibility valuation of a residue \(x\in R\), with \(\nu_p(0)=k\). The second-coordinate map is therefore strictly contracting for the truncated \(p\)-adic metric. Every such map is given uniquely by independent digit choices
\[
 b(a)=\sum_{j=0}^{k-1}p^j\beta_j(a\bmod p^j),\qquad
 \beta_j:\mathbb Z/p^j\mathbb Z\longrightarrow\{0,1,\ldots,p-1\}.
\]
At \(j=0\), the domain is the one-point ring. The exact number of distinct *unordered frequency sets*, counting neither a change of ordering nor an external equivalence relation, is
\[
\boxed{\mathcal N(p,k)=p^{\sum_{j=0}^{k-1}p^j}=p^{(p^k-1)/(p-1)}.}
\]
Among these, exactly \(p^{2k-1}\) are affine graphs \(b(a)=c+ua\): they have arbitrary \(c\in R\) and \(u\in pR\). In particular, \(\mathcal N(3,2)=81\), of which \(27\) are affine and \(54\) are nonaffine.

## Assumptions and scope

The ambient group is the additive group \(R^2\), with the standard nondegenerate additive pairing \((a,b)\cdot(x,y)=ax+by\bmod q\). The characteristic prime must be odd; this proof does not classify characteristic-two moduli. Frequencies are identified as elements of \(R^2\), not modulo shifts, isometries, or changes of basis. The result concerns *all* sets of \(q\) pairwise orthogonal additive characters on this fixed parabola, not arbitrary spectral subsets of \(R^2\).

## Proof

**1. Exact quadratic Fourier-zero criterion.** For \(A,B\in R\) write
\[
S_q(A,B)=\sum_{t\in R}\exp\!\left(\frac{2\pi i}{q}(At+Bt^2)\right).
\]
Set \(r=\nu_p(A)\) and \(j=\nu_p(B)\), allowing either to equal \(k\) at zero. We claim the exact equivalence
\[
\boxed{S_q(A,B)=0\quad\Longleftrightarrow\quad r<j.}
\]
If \(r<j\), put \(h=p^{k-r-1}\). Under translation \(t\mapsto t+h\), the linear exponent changes by \(Ah\), an integer of valuation exactly \(k-1\); the quadratic change is \(B(2th+h^2)\), divisible by \(p^k\) because \(j\ge r+1\). Thus translation multiplies \(S_q(A,B)\) by the nontrivial \(p\)-th root \(\exp(2\pi i Ah/q)\), so the sum is zero.

Conversely, suppose \(r\ge j\). If \(j=k\), both coefficients vanish and \(S_q(A,B)=q\ne0\). Otherwise, divide both coefficients by \(p^j\), set \(m=p^{k-j}\), and note \(B'=B/p^j\) is a unit modulo \(m\). The original sum equals \(p^j\) times
\[
\sum_{t\bmod m}\exp\!\left(\frac{2\pi i}{m}(A't+B't^2)\right).
\]
Since \(2B'\) is invertible, completing the square makes the magnitude equal to the magnitude of the primitive quadratic Gauss sum \(G_m(B')=\sum_t\exp(2\pi iB't^2/m)\). The bijective substitution \((t,s)\mapsto(t-s,t+s)\) over odd \(m\) gives
\[
|G_m(B')|^2=\sum_{u,v\bmod m}\exp(2\pi i B'uv/m)=m>0.
\]
Therefore the original sum is nonzero. This proves the zero criterion without approximations.

**2. Rigidity of frequency coordinates.** Orthogonality of two distinct normalized characters \(\phi_{a,b}\) and \(\phi_{a',b'}\) is exactly \(S_q(a-a',b-b')=0\). By Step 1, this requires \(\nu_p(a-a')<\nu_p(b-b')\). In particular two distinct orthogonal frequencies cannot share their first coordinate. Any orthogonal set of size \(q\) therefore contains exactly one frequency above each \(a\in R\), hence is a graph. The same criterion says the graph is pairwise orthogonal precisely when its coordinate map is strictly contracting. As \(\ell^2(E)\) has dimension \(q\), a family of \(q\) unit-norm pairwise orthogonal vectors is automatically a basis.

**3. Characterization and enumeration of contractions.** Strict contraction is equivalent, for each \(0\le j<k\), to
\[
a\equiv a'\pmod{p^j}\quad\Longrightarrow\quad b(a)\equiv b(a')\pmod{p^{j+1}}.
\]
For \(j=0\), this forces the first output digit to be constant. At general \(j\), the \(j\)-th base-\(p\) digit of \(b(a)\) depends only on \(a\bmod p^j\). Conversely, independently prescribing functions \(\beta_j\) on these residue classes enforces every congruence above, hence strict contraction. There are \(p^{p^j}\) choices at level \(j\), independently, yielding exactly \(\prod_{j=0}^{k-1}p^{p^j}\) distinct maps and frequency sets.

For affine maps \(b(a)=c+ua\), strict contraction is equivalent to \(p\mid u\), by testing a unit difference and then multiplying arbitrary differences. There are \(p^k\) choices of \(c\) and \(p^{k-1}\) of \(u\), giving \(p^{2k-1}\) affine graphs. This completes every assertion.

## Verification

The standalone Python 3 program `check_spectra.py` verifies the finite cases without floating-point evaluation. It uses the exact coefficient criterion for divisibility by the cyclotomic polynomial \(\Phi_{p^k}(X)=\sum_{s=0}^{p-1}X^{s p^{k-1}}\) to decide whether \(S_q(A,B)\) is zero. Reproduce from these files with `python3 check_spectra.py`.

The tested parameter pairs \((p,k)\) are \((3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\). The program compares the criterion against exact cyclotomic cancellation for all \(1518\) coefficient pairs; constructs and checks all \(89\) digit-map spectra in the small enumerated cases; tests \(64\) additional sampled spectra; and independently enumerates the complete spectrum counts \(81\) for \((3,2)\) and \(5\) for \((5,1)\). These tests corroborate the exact proof but do not prove the unrestricted statement by enumeration.

## Relationship to prior work

Iosevich and Koh study extension estimates on finite-field quadratic surfaces, using quadratic Fourier sums; their norm estimates over fields do not classify all orthogonal frequency sets on this prime-power ring parabola. Cai, Chen, Lipton, and Lu study the evaluation and cancellation of quadratic exponential sums, providing an established analytic ingredient but no partner-spectrum enumeration. Aten and collaborators study spectral sets and graph constructions in vector spaces over prime fields; the setting and classification problem differ. Fan, Fan, and Shi prove spectral/tiling and spectral-partner structure theorems in one-dimensional \(p\)-adic fields and cyclic prime-power rings; their results do not directly describe the frequency graph of the present two-coordinate polynomial curve. The novelty assessed here is the simultaneous *complete* basis-partner classification and exact counting in the two-coordinate prime-power ring family, not quadratic Gauss-sum evaluation by itself.

## Limitations

The theorem is restricted to odd prime powers and the quadratic graph with unit leading coefficient. It does not address nonlinear polynomials of other degrees, arbitrary two-dimensional spectral sets, characteristic two, or equivalence-class counts under affine transformations. A semantically equivalent formulation in older spectral/Butson matrix or \(p\)-adic character literature remains a historical-priority risk; absence from searches is not proof of priority. 

## References

- Alex Iosevich and Doowon Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, publicly posted 2008-04-28, https://arxiv.org/abs/0804.4505.
- Jin-Yi Cai, Xi Chen, Richard Lipton, and Pinyan Lu, *On Tractable Exponential Sums*, arXiv:1005.2632v1, publicly posted 2010-05-14, https://arxiv.org/abs/1005.2632.
- C. Aten and collaborators, *Tiling sets and spectral sets over finite fields*, arXiv:1509.01090v1, publicly posted 2015-09-03, https://arxiv.org/abs/1509.01090.
- Aihua Fan, Shilei Fan, and Ruxi Shi, *Compact Open Spectral Sets in \(\mathbb Q_p\)*, arXiv:1511.04837v1, publicly posted 2015-11-16, https://arxiv.org/abs/1511.04837.
