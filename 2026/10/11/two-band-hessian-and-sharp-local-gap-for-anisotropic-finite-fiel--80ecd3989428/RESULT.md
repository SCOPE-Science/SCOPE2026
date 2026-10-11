# Two-band Hessian and sharp local gap for anisotropic finite-field paraboloid extension

## Finding

Let \(q\) be an odd prime power with \(q\equiv3\pmod4\), and let \(V=\mathbb F_q^2\). For \(Q(u)=u_1^2+u_2^2\), fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\) and put
\[
\mathcal E_qf(X,t)=q^{-2}\sum_{u\in V}f(u)\psi(X\cdot u+tQ(u)),\qquad
C_q=1+q^{-1}-q^{-2}.
\]
The sharp extension deficit is
\[
\mathfrak D_q(f)=C_q\left(q^{-2}\sum_{u\in V}|f(u)|^2\right)^2-
\sum_{(X,t)\in\mathbb F_q^3}|\mathcal E_qf(X,t)|^4.
\]
For every complex-valued \(g=r+is\) on \(V\), where \(r,s\) are real-valued and each has zero mean, the second-order expansion at the constant extremizer is
\[
\boxed{\mathfrak D_q(1+\varepsilon g)=\varepsilon^2\left[
\left(2-\frac2q+\frac4{q^2}\right)q^{-2}\sum_{u\in V}r(u)^2
+\left(2-\frac2q\right)q^{-2}\sum_{u\in V}s(u)^2
\right]+O_{q,g}(\varepsilon^3).}
\]
Here \(\varepsilon\) is real and tends to zero. With the normalized real Hilbert-space inner product \(q^{-2}\sum\operatorname{Re}(g\overline h)\), the half-Hessian \(\frac12D^2\mathfrak D_q(1)\) has exactly three eigenvalues: \(0\) with multiplicity \(2\), \(2-2/q\) with multiplicity \(q^2-1\), and \(2-2/q+4/q^2\) with multiplicity \(q^2-1\). Its kernel is precisely the two-real-dimensional space of constant complex perturbations. The optimal transverse quadratic coercivity coefficient is \(2-2/q\), attained by every nonzero, purely imaginary, mean-zero perturbation.

## Assumptions and scope

All sums use counting measure except the explicitly normalized \(q^{-2}\) averages. No assumption that \(q\) is prime is made. The quadratic form \(Q\) is anisotropic because \(-1\) is not a square when \(q\equiv3\pmod4\). The coefficient in the displayed expansion is the quadratic Taylor coefficient, not the eigenvalue of the full second derivative (which is twice that coefficient). The sharp global inequality \(\mathfrak D_q(f)\ge0\), including the value of \(C_q\), is established in González-Riquelme and Oliveira e Silva, Theorem 1.1; the new assertion concerns its complete local curvature.

## Proof

**1. Exact fourth-moment formula.** For \(c\in V\) and \(t\in\mathbb F_q\), write \(S_t=\{h\in V:Q(h)=t\}\), \(L_t=|S_t|\), and
\[
A_f(c,t)=\sum_{h\in S_t}f(c+h)f(c-h).
\]
Character orthogonality on \(\mathbb F_q^3\), followed by the bijection from ordered pairs \((u,v)\) to center \(c=(u+v)/2\) and half-difference \(h=(u-v)/2\), gives the **exact identity**
\[
\sum_{X,t}|\mathcal E_qf(X,t)|^4=q^{-5}\sum_{c\in V}\sum_{\tau\in\mathbb F_q}|A_f(c,\tau)|^2.
\tag{1}
\]
Indeed \(Q(c+h)+Q(c-h)=2Q(c)+2Q(h)\), so equality of pair sums and pair energies is precisely equality of \(c\) and \(Q(h)\). There are no hidden factors of two: ordered pairs and center/half-difference pairs are bijective because the characteristic is odd.

**2. Anisotropic shell counts.** Identifying \(u_1+iu_2\) with an element of \(\mathbb F_{q^2}\), where \(i^2=-1\), identifies \(Q\) with its field norm to \(\mathbb F_q\). The multiplicative norm map has kernel of order \(q+1\). Therefore
\[
L_0=1,\qquad L_t=q+1\quad(t\ne0),\qquad
\sum_tL_t^2=1+(q-1)(q+1)^2=q^3+q^2-q.
\tag{2}
\]
In particular, (1) gives \(\sum|\mathcal E_q1|^4=C_q\) exactly.

**3. Two elementary collision identities.** Let \(h:V\to\mathbb R\) have \(\sum h=0\), and write \(H(h)=\sum h(u)^2\). Then
\[
\sum_{c,t}\left(\sum_{v\in S_t}h(c+v)\right)^2=q(q-1)H(h).
\tag{3}
\]
To verify this, fix an ordered pair of arguments \((x,y)\). The coefficient of \(h(x)h(y)\) on the left is the number of \((v,w)\) with \(v-w=x-y\) and \(Q(v)=Q(w)\). It is \(q^2\) when \(x=y\). For \(x\ne y\), the equation \(Q(w+x-y)=Q(w)\) is a nontrivial affine linear equation in the two coordinates of \(w\), and has exactly \(q\) solutions. Hence the left side is \((q^2-q)H(h)+q(\sum h)^2\), which proves (3).

The second identity is
\[
\sum_{c,t}L_t\sum_{v\in S_t}h(c+v)h(c-v)=-qH(h).
\tag{4}
\]
Indeed \((c,v)\mapsto (c+v,c-v)\) is a bijection on ordered pairs, and \(L_{Q(v)}=q+1-q\mathbf1_{v=0}\). Consequently the sum equals \((q+1)(\sum h)^2-qH(h)\).

**4. Exact quadratic coefficient.** Put \(f=1+\varepsilon(r+is)\), with \(\sum r=\sum s=0\). For each center and shell, (1) gives
\[
A_f(c,t)=L_t+2\varepsilon\sum_{v\in S_t}(r+is)(c+v)
+\varepsilon^2\sum_{v\in S_t}(r+is)(c+v)(r+is)(c-v).
\]
The real quadratic coefficient in \(\sum_{c,t}|A_f(c,t)|^2\) is
\[
4q(q-1)(H(r)+H(s))-2qH(r)+2qH(s)
=q(4q-6)H(r)+q(4q-2)H(s),
\tag{5}
\]
by (3) and (4). Meanwhile the quadratic coefficient in \(C_q(q^{-2}\sum|f|^2)^2\) is \(2C_qq^{-2}(H(r)+H(s))\). Combining (1) and (5) yields precisely the two displayed coefficients in the finding.

**5. Kernel and sharpness.** Every constant complex perturbation is a null direction because the deficit vanishes on all scalar multiples of \(1\). Conversely, writing an arbitrary perturbation as its complex constant mean plus a zero-mean part, homogeneity \(\mathfrak D_q(\lambda f)=|\lambda|^4\mathfrak D_q(f)\) shows that the constant component contributes no quadratic term or mixed term. Both nonconstant coefficients are strictly positive, as \(q\ge3\), so these are all null directions. Orthogonality of the real and imaginary mean-zero subspaces gives the eigenvalue multiplicities. Since \(2-2/q<2-2/q+4/q^2\), the lower eigenvalue is the exact local minimum, achieved in every imaginary mean-zero direction.

## Verification

The accompanying standalone \(verify.py\) enumerates every shell and center using exact integer arithmetic for \(\mathbb F_3,\mathbb F_7,\mathbb F_{11}\) and the non-prime field \(\mathbb F_{27}\). It checks the shell counts, the constant fourth moment, and both exact second-order coefficients for mean-zero test perturbations. All checks passed. Separate direct evaluations of the original extension sum at small real perturbations over \(\mathbb F_3\) and \(\mathbb F_7\) agreed with the predicted quadratic limits to numerical precision. These are finite checks, not substitutes for the all-field proof above.

## Relationship to prior work

González-Riquelme and Oliveira e Silva (2024), Theorem 1.1 and Section 4.1, prove the exact sharp \(L^2\to L^4\) inequality for this paraboloid and exhibit constant extremizers; their proof uses the same anisotropic shell cardinalities. The result here does not re-claim the best global constant or the fact of extremality. Rather, it determines the complete real Hessian spectrum, its kernel and multiplicities, and the optimal second-order gap distinguishing amplitude and phase directions. Results on the split hyperbolic paraboloid or higher-moment finite-field curves use different collision geometry and do not directly yield this anisotropic two-band formula.

## Limitations

The statement concerns the second differential at a nonzero constant extremizer only. It does **not** assert a sharp global stability inequality, an explicit uniform neighborhood radius in \(q\), or a classification of all nonconstant global extremizers. The displayed sharp local gap is relative to the normalized real Hilbert metric and to perturbations transverse to complex scalar multiplication. An equivalent unindexed or differently normalized local-curvature identity remains a possible literature overlap.

## References

González-Riquelme, Cristian, and Diogo Oliveira e Silva. *Sharp extension inequalities on finite fields*. arXiv:2405.16647, first posted 2024-05-26; especially Theorem 1.1 and Section 4.1. https://arxiv.org/abs/2405.16647
