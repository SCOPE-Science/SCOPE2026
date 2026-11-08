# A five-residue discrete-Gaussian law for Heisenberg Lie retractions

## Finding

Let \(q\) be any prime power and \(m\ge1\). For the \((2m+1)\)-dimensional Heisenberg Lie algebra \(H_m(q)\) over \(\mathbb F_q\), the rank of a uniformly sampled idempotent endomorphism has an explicit finite distribution and a sharp five-residue discrete-Gaussian limit as \(m\to\infty\), with \(q\) fixed.

Write \(b_{m,r}\) for the number of idempotent endomorphisms with image dimension \(r\). For \(0\le r\le m\),
\[
b_{m,r}=q^{r(2m-r+1)}\prod_{i=0}^{r-1}\frac{q^{2(m-i)}-1}{q^{r-i}-1}.
\]
The empty product is \(1\), and there is precisely one further idempotent, the identity of image dimension \(2m+1\). All other ranks vanish. Thus \(N_m=1+\sum_{r=0}^m b_{m,r}\).

Set
\[
\rho_m=\frac{8m+3}{10},\quad a_m=\lfloor\rho_m\rfloor,\quad\delta_m=\rho_m-a_m,\quad D_q=\prod_{j\ge1}(1-q^{-j}),\quad
\Theta_{q,\delta}=\sum_{j\in\mathbb Z}q^{-\frac52(j-\delta)^2}.
\]
For each fixed prime power \(q\),
\[
N_m\sim \frac{\Theta_{q,\delta_m}}{D_q}\,q^{(8m+3)^2/40}.
\]
Along each fixed congruence class of \(m\) modulo \(5\), the integer-valued variable \(R_m-a_m\) converges **in total variation** to the probability mass function
\[
\Pr(X=j)=\frac{q^{-\frac52(j-\delta_m)^2}}{\Theta_{q,\delta_m}},\qquad j\in\mathbb Z,
\]
where \(\delta_m\) is constant on the chosen congruence class. Hence \(R_m/m\to4/5\) in probability.

The event of maximal proper retraction rank has the sharper tail
\[
\Pr(R_m=m)\sim
\frac{\prod_{j\ge1}(1-q^{-2j})}{\Theta_{q,\delta_m}}
q^{-(2m-3)^2/40}.
\]

## Assumptions and scope

The Lie algebra is \(H_m(q)=V\oplus\mathbb F_qz\), with \(\dim_{\mathbb F_q}V=2m\) and bracket \([v+az,w+bz]=\omega(v,w)z\), where \(\omega\) is a fixed nondegenerate alternating bilinear form. This is a genuine Lie bracket also in characteristic two. Endomorphisms are \(\mathbb F_q\)-linear and bracket-preserving. Idempotence means \(P^2=P\). The image rank includes the central coordinate. The field order \(q\) is fixed in all limits; \(m\) ranges over positive integers. These hypotheses exclude nonlinear and merely additive maps.

## Proof

**1. Classification.** Since \([H_m(q),H_m(q)]=\mathbb F_qz\), any endomorphism has the unique form
\[
P(z)=cz,\qquad P(v)=Av+\varphi(v)z,
\]
with \(c\in\mathbb F_q\), \(A\in\operatorname{End}_{\mathbb F_q}(V)\), \(\varphi\in V^*\). Bracket preservation is equivalent to \(\omega(Av,Aw)=c\omega(v,w)\) for all \(v,w\). The idempotence identities are \(c^2=c\), \(A^2=A\), and \(\varphi\circ A+c\varphi=\varphi\). Thus \(c=0\) or \(1\).

If \(c=1\), preservation of the nondegenerate form forces \(A\) invertible. Then \(A^2=A\) forces \(A=I\), and the last identity forces \(\varphi=0\): this is the identity map. If \(c=0\), the image \(U=\operatorname{im}A\) is totally isotropic, \(A\) is a projection onto \(U\), and \(\varphi=\psi\circ A\) for a unique \(\psi\in U^*\). The image of \(P\) is the graph of \(\psi\) over \(U\), of rank \(r=\dim U\le m\). Conversely every such pair gives an idempotent Lie endomorphism, without any restriction on the characteristic.

**2. Rank counts.** An isotropic \(r\)-subspace \(U\subset V\) can be counted using ordered isotropic frames. After choosing an \(i\)-dimensional isotropic span, the next vector has \(q^{2m-i}-q^i\) choices. Divide by the \(\prod_{i=0}^{r-1}(q^r-q^i)\) ordered bases of \(\mathbb F_q^r\), giving
\[
I_{m,r}=\prod_{i=0}^{r-1}\frac{q^{2(m-i)}-1}{q^{r-i}-1}.
\]
For fixed \(U\), projections \(A:V\to U\) restricting to the identity on \(U\) form an affine space of dimension \(r(2m-r)\), hence have \(q^{r(2m-r)}\) possibilities. The independent choice \(\psi\in U^*\) contributes \(q^r\). This yields the exact formula, including \(r=0\).

**3. A centered weight.** Elementary extraction of powers of \(q\) gives
\[
b_{m,r}=q^{F_m(r)}C_{m,r},\quad
F_m(r)=4mr-\frac52r^2+\frac32r=\frac{(8m+3)^2}{40}-\frac52(r-\rho_m)^2,
\]
\[
C_{m,r}=\frac{\prod_{i=0}^{r-1}(1-q^{-2(m-i)})}{\prod_{j=1}^r(1-q^{-j})}.
\]
For all \(0\le r\le m\), \(0<C_{m,r}\le D_q^{-1}\). When \(r=a_m+j\) with fixed integer \(j\), both \(r\) and \(m-r\) tend to infinity, so \(C_{m,r}\to D_q^{-1}\). The centered weights are bounded by \(D_q^{-1}q^{-\frac52(j-\delta_m)^2}\). This is summable uniformly over all five possible \(\delta_m\). Dominated convergence for the extended integer sum proves the sharp total count; the extra identity contributes only \(1\), negligible against the total. Applying the same domination to absolute mass differences gives total-variation convergence. Gaussian tails imply \(R_m-a_m=O_{\Pr}(1)\), so \(R_m/m\to4/5\).

**4. Extreme image rank.** For \(r=m\), \(C_{m,m}\to \prod_{j\ge1}(1-q^{-2j})/D_q\), whereas \(m-\rho_m=(2m-3)/10\). Dividing \(b_{m,m}\) by the just-proved asymptotic for \(N_m\) gives the displayed maximal-rank tail with its leading constant. This also proves \(m^{-2}\log_q\Pr(R_m=m)\to-1/10\).

## Verification

Run `python3 verify.py` using a standard Python 3 interpreter. The checker enumerates every linear map on the three-dimensional Heisenberg Lie algebra over \(\mathbb F_2\) and \(\mathbb F_3\), applies the brackets and idempotence directly, and checks the rank counts. For the five-dimensional algebra over \(\mathbb F_2\), it exhausts all \(4\times4\) induced maps, both central scalars, and all central linear forms, testing the bracket and idempotence identities independently of the counting formula. It also compares normalized exact weights with the asymptotic five-residue discrete Gaussian for \(m=10,20,40\) over \(\mathbb F_2\). Observed counts are \(1,12,1\) at ranks \(0,1,3\) over \(\mathbb F_2\); \(1,36,1\) at ranks \(0,1,3\) over \(\mathbb F_3\); and \(1,240,960,1\) at ranks \(0,1,2,5\) for the five-dimensional binary case. Execution prints `VERIFY_OK`.

These are finite checks, not an infinite-dimensional proof. The asymptotic statements follow from the argument above.

## Relationship to prior work

Anil Kumar and Pradhan (2019), arXiv:1908.00331, give explicit endomorphism parametrizations for odd-prime exponent-\(p\) extraspecial Heisenberg groups, count total endomorphisms, and establish isotropic-subspace counts. Via the class-two group/Lie correspondence in odd characteristic, their framework strongly anticipates the linear-algebra reduction used above. The isotropic count and symplectic-similitude dichotomy are **prior mathematics**, not new claims here. The exact idempotent specialization is supplied to support the genuinely separate limiting statement: the five-residue discrete-Gaussian rank distribution, the \(4/5\) rank fraction, and the sharp rare maximal-rank law. Their Theorems \(\Omega\), \(5.2\), and \(5.3\) do not state these limiting laws.

Kaygorodov and Khudoyberdiyev (2023), arXiv:2310.00624, study transposed Poisson structures and half-derivations on oscillator Lie algebras with Heisenberg ideals, over \(\mathbb C\); they do not examine random finite-field retracts. He, Zhang and Zhang (2022), DOI 10.1080/03081087.2022.2112016, study inclusion graphs of isotropic subspaces, not distributions of idempotent Lie endomorphisms. No claim of absolute publication priority follows from unsuccessful searches; an unlocated general theorem on random symplectic retractions is a remaining possibility.

## Limitations

The theorem is specific to the nondegenerate single-center Heisenberg family and to linear Lie homomorphisms. The field order \(q\) must be fixed as \(m\) grows. The limiting distribution oscillates among five residue classes; there is no single unshifted limit. A published endomorphism classification for the related odd-prime Heisenberg group provides substantial prior groundwork. No independent mathematical audit has been performed and wider publication priority is not certified.

## References

1. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits* (first public August 1, 2019), arXiv:1908.00331, especially Theorem \(\Omega\) and Section 5.
2. I. Kaygorodov and A. Khudoyberdiyev, *Transposed Poisson structures on solvable and perfect Lie algebras* (first public October 1, 2023), arXiv:2310.00624.
3. J. He, S. Zhang, and G. Zhang, *Symplectic totally isotropic subspace inclusion graph*, Linear and Multilinear Algebra (online August 16, 2022), DOI: 10.1080/03081087.2022.2112016.
