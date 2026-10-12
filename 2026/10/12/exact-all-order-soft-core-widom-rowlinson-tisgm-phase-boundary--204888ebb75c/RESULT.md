# Exact all-order soft-core Widom–Rowlinson TISGM phase boundary

## Finding

Consider the ferromagnetic soft-core Widom–Rowlinson model on a Cayley tree of integer order \(k\ge4\), with interaction parameter \(0<\theta<1\) and activity \(\lambda>0\). The translation-invariant splitting Gibbs measures are represented by the positive boundary-law system studied by Kissel, Külske and Rozikov.

Put
\[
\theta_c(k)=\frac{k-1}{k+1}.
\]
If \(\theta\ge\theta_c(k)\), there is exactly one tree-automorphism-invariant splitting Gibbs measure (TISGM) for every \(\lambda>0\). If \(0<\theta<\theta_c(k)\), put
\[
\lambda_c(k,\theta)=\frac{1}{k-1-(k+1)\theta}\left(\frac{k+1}{k}\right)^k.
\]
Then there is exactly one TISGM for
\[
0<\lambda\le\lambda_c(k,\theta),
\]
and exactly three TISGMs for
\[
\lambda>\lambda_c(k,\theta).
\]
This proves the soft-core ferromagnetic content of Conjecture 1 in the source for every \(k\ge4\). The two nonsymmetric measures above threshold are exchanged by the \(+/-\) spin symmetry.

## Assumptions and scope

The statement concerns only tree-automorphism-invariant splitting Gibbs measures of the ferromagnetic soft-core model, so \(k\ge4\), \(0<\theta<1\), and \(\lambda>0\). It does not classify periodic or nonperiodic splitting measures, all Gibbs measures, extremality of the three TISGMs, dynamical Gibbs--non-Gibbs behavior, or the antiferromagnetic model.

The same algebra has a hard-core limit at \(\theta=0\), but the claimed novelty is restricted to the soft-core regime because hard-core uniqueness/nonuniqueness results have separate prior literature.

## Proof

Use the source variables \(u,v>0\) and \(a=\lambda^{1/k}>0\). The positive TISGM boundary laws satisfy
\[
u=a\frac{1+u^k+\theta v^k}{1+u^k+v^k},\qquad
v=a\frac{1+\theta u^k+v^k}{1+u^k+v^k}.
\]
First consider the symmetric branch \(u=v=r\). Solving for \(a\) gives
\[
a(r)=r\frac{1+2r^k}{1+(1+\theta)r^k}.
\]
Its logarithmic derivative is
\[
\frac{a'(r)}{a(r)}=\frac1r+\frac{2kr^{k-1}}{1+2r^k}-\frac{k(1+\theta)r^{k-1}}{1+(1+\theta)r^k}>0,
\]
because the difference of the last two fractions has numerator proportional to \(1-\theta>0\). Hence for each \(a>0\) there is exactly one symmetric positive solution.

Now suppose \(u\ne v\). Let
\[
S_n(u,v)=\sum_{j=0}^{n}u^{n-j}v^j.
\]
Solving the two source equations linearly for \(a\) and \(a\theta\), exactly as in the source's attempted proof of its conjecture, gives
\[
a=\frac{S_k(u,v)}{S_{k-1}(u,v)},\qquad
a\theta=\frac{uvS_{k-2}(u,v)-1}{S_{k-1}(u,v)}.
\]
Write \(v=uq\) with \(q>0\), and define
\[
D_k(q)=\sum_{j=0}^{k}q^j,\qquad
E_k(q)=\sum_{j=0}^{k-1}q^j,\qquad
C_k(q)=\sum_{j=1}^{k-1}q^j.
\]
The relation \((a\theta)/a=\theta\) becomes
\[
u^k\bigl(C_k(q)-\theta D_k(q)\bigr)=1.
\]
Thus a nonsymmetric solution exists only when
\[
H_\theta(q):=C_k(q)-\theta D_k(q)>0,
\]
and then \(u^k=H_\theta(q)^{-1}\). Substitution into \(a^k=\lambda\) yields the exact one-variable branch
\[
\Lambda_\theta(q):=\lambda
=\frac{D_k(q)^k}{E_k(q)^k H_\theta(q)}.
\]
Conversely, any \(q>0\), \(q\ne1\), with \(H_\theta(q)>0\), together with \(u^k=H_\theta(q)^{-1}\) and \(a=uD_k(q)/E_k(q)\), reconstructs a positive solution of the original two equations. Also
\[
\Lambda_\theta(q)=\Lambda_\theta(q^{-1}),
\]
so it suffices to count \(q>1\).

The physical domain is already enough to determine the temperature boundary. Put \(q=e^{2x}\), \(x>0\). Then
\[
\frac{C_k(q)}{D_k(q)}=\frac{\sinh((k-1)x)}{\sinh((k+1)x)}.
\]
The function \(y\mapsto y\coth y\) is strictly increasing for \(y>0\), hence the displayed ratio is strictly decreasing in \(x>0\), from
\[
\frac{k-1}{k+1}
\]
to zero. Therefore no nonsymmetric solution exists when \(\theta\ge\theta_c(k)\). If \(0<\theta<\theta_c(k)\), there is a unique \(q_\theta>1\) with \(H_\theta(q_\theta)=0\), and the physical ratio interval is \(1<q<q_\theta\).

It remains to prove that \(\Lambda_\theta\) has no extra turns on this interval. Differentiation gives
\[
\frac{\Lambda_\theta'(q)}{\Lambda_\theta(q)}
=k\frac{D_k'(q)}{D_k(q)}-k\frac{E_k'(q)}{E_k(q)}-\frac{H_\theta'(q)}{H_\theta(q)}.
\]
After multiplication by the positive denominator \(D_kE_kH_\theta\), the numerator is
\[
N_\theta(q)=k\bigl(D_k'E_k-D_kE_k'\bigr)H_\theta-H_\theta'D_kE_k.
\]
A direct coefficient collection gives the exact identity
\[
\frac{N_\theta(q)}{q-1}
=(1-\theta)D_k(q)P_k(q)+kq^{k-1}R_k(q),
\]
where
\[
R_k(q)=\sum_{j=0}^{k-2}(j+1)(k-1-j)q^j
\]
and
\[
P_k(q)=
\sum_{i=0}^{k-2}\binom{i+3}{3}q^i+
\sum_{i=k-1}^{2k-4}\binom{2k-1-i}{3}q^i.
\]
Every coefficient of \(P_k\) and \(R_k\) is positive. Since \(0<\theta<1\) and \(q>1\), this proves \(N_\theta(q)>0\) and therefore
\[
\Lambda_\theta'(q)>0
\]
throughout the physical interval.

Finally,
\[
\lim_{q\downarrow1}\Lambda_\theta(q)
=\frac{(k+1)^k}{k^k\bigl(k-1-(k+1)\theta\bigr)}
=\lambda_c(k,\theta),
\]
while \(\Lambda_\theta(q)\to\infty\) as \(q\uparrow q_\theta\). Hence for \(\lambda\le\lambda_c\) there is no nonsymmetric pair, while for \(\lambda>\lambda_c\) there is exactly one ratio \(q>1\), together with its reciprocal \(q^{-1}\), giving exactly two nonsymmetric solutions. Adding the unique symmetric solution proves the one-versus-three classification.

## Verification

The bundled `verify.py` independently expands the derivative numerator from \(D_k,E_k,C_k\) and checks, with exact integer polynomial arithmetic, the stated positive-coefficient factorization for every integer \(4\le k\le200\). It also verifies reciprocal symmetry and representative branch reconstructions. These finite checks corroborate the algebra; the proof for all \(k\ge4\) is the displayed coefficient identity and positivity argument, not extrapolation from the checked range.

The source's own finite Mathematica evidence covered only \(k=4,\ldots,15\); the proof above does not use those computations.

## Relationship to prior work

Kissel, Külske and Rozikov derive the same two-variable system, prove exact one/three results for \(k=2,3\), and for \(k\ge4\) prove a sufficient nonuniqueness region with the same critical curve. Their Theorem 6 states only “at least three” above that curve and leaves exact one-versus-three counting as Conjecture 1. Their attempted proof reduces the problem to a constrained minimum and reports numerical verification only for \(k=4,\ldots,15\). The ratio parameterization above replaces that unresolved constrained minimization by a global one-variable monotonicity theorem.

The first author's 2019 doctoral thesis repeats the same conjecture and the same unresolved constrained-minimum step. Later work on dynamical Gibbs--non-Gibbs transitions for Widom--Rowlinson models on trees concerns a different question and does not imply the static TISGM count proved here.

## Limitations

This result counts only TISGMs represented by the source's translation-invariant boundary laws. It does not establish extremality of any of the three measures, classify non-translation-invariant splitting measures, or describe all Gibbs measures in the coexistence region. The hard-core endpoint \(\theta=0\) is not included in the novelty claim. A weakly indexed later resolution under another parameterization remains a residual literature-search risk.

## References

1. S. Kissel, C. Külske and U. A. Rozikov, “Hard-Core and Soft-Core Widom-Rowlinson models on Cayley trees”, arXiv:1901.09258v1; Journal of Statistical Mechanics: Theory and Experiment (2019), 043204, DOI:10.1088/1742-5468/ab081e.
2. S. J. Kissel, “Hard-core and soft-core Widom-Rowlinson models in various geometries”, doctoral thesis, Ruhr University Bochum, April 2019, German National Library record 1189421666.
3. S. Bergmann, S. Kissel and C. Külske, “Dynamical Gibbs–non-Gibbs transitions in Widom–Rowlinson models on trees”, arXiv:2012.09718; Annales de l’Institut Henri Poincaré, Probabilités et Statistiques 59 (2023).