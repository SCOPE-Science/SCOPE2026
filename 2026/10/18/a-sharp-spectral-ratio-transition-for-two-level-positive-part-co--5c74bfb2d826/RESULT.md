# A sharp spectral-ratio transition for two-level positive-part conditioning

## Finding
Let \(\mathcal H_2\) be the real Banach space of complex Hermitian \(2\times2\) matrices, equipped with a Schatten norm \(\|\cdot\|_p\), where \(p\in\{1,2,\infty\}\). Define the spectral clipping map \(F(A)=A_+=\tfrac12(A+|A|)\). For every invertible indefinite \(A\in\mathcal H_2\), write its two eigenvalues as \(a>0\) and \(-b<0\), and set \(q=a/(a+b)\in(0,1)\).

**The sharp local conditioning profile is**
\[
\boxed{\|DF(A)\|_{\infty\to\infty}=\|DF(A)\|_{1\to1}=K(q),\qquad \|DF(A)\|_{2\to2}=1,}
\]
where
\[
\boxed{K(q)=\begin{cases}1,&0<q\le1/\sqrt2,\\[2pt]
\dfrac{2q^2}{\sqrt{4q^2-1}},&1/\sqrt2<q<1.\end{cases}}
\]
Consequently, the spectral positive-part map is locally expansive in either the operator or trace norm precisely when
\[
\boxed{a/b>1+\sqrt2.}
\]
The two branches coincide continuously at the transition, and the displayed constants are attained by explicit infinitesimal perturbations of every such \(A\). Furthermore, on the entire space \(\mathcal H_2\), including singular and definite matrices, the sharp pairwise Lipschitz constants are
\[
\boxed{\operatorname{Lip}_{\infty}(F)=\operatorname{Lip}_{1}(F)=\frac2{\sqrt3},\qquad \operatorname{Lip}_{2}(F)=1.}
\]
The **ratio-dependent local profile and its precise transition** are the substantive assertion here; the endpoint constant \(2/\sqrt3\) is closely related to a classical two-by-two triangular Schur-multiplier norm and is not presented as an unrelated new multiplier constant.

## Assumptions and scope
The matrices are Hermitian over \(\mathbb C\); restricting all statements to real symmetric matrices gives the same constants and the same explicit extremizers. The Schatten norm \(\|X\|_p\) is the \(\ell_p\)-norm of the singular values, with \(p=\infty\) meaning the operator norm. The induced derivative norm is \(\|DF(A)\|_{p\to p}:=\sup_{H=H^*,\,H\ne0}\|DF(A)[H]\|_p/\|H\|_p\), where the derivative is taken as a real Fréchet derivative on \(\mathcal H_2\). For the local statement, \(A\) must have one strictly positive and one strictly negative eigenvalue. Definite matrices have derivative \(I\) or \(0\), respectively; singular matrices are included only in the global Lipschitz statement. No assertion is made for non-Hermitian matrices or dimension greater than two.

## Proof
**1. The derivative is a one-parameter Schur multiplier.** Unitary conjugation leaves all the relevant norms unchanged, so take \(A=\operatorname{diag}(a,-b)\). The usual divided-difference formula for the Fréchet derivative of a spectral function, applied to \(f(t)=\max(t,0)\) at the two nonzero eigenvalues, gives for every Hermitian \(H=(h_{ij})\)
\[
DF(A)[H]=L_q(H):=\begin{pmatrix}h_{11}&qh_{12}\\q\overline{h_{12}}&0\end{pmatrix},
\quad q=\frac{f(a)-f(-b)}{a-(-b)}=\frac a{a+b}.
\]
The formula can alternatively be obtained directly by differentiating the positive eigenvalue and its rank-one spectral projector; hence it does not require differentiability of \(f\) at zero. Because \(L_q\) multiplies matrix entries by \(1,q,q,0\), the Hilbert–Schmidt norm obeys \(\|L_q(H)\|_2\le\|H\|_2\), with equality at \(H=\operatorname{diag}(1,0)\). Thus \(\|L_q\|_{2\to2}=1\).

**2. Sharp operator-norm profile.** The closed unit ball of Hermitian \(2\times2\) matrices is the convex hull of its Hermitian unitary extreme points. Besides \(\pm I\), every such point, after diagonal phase conjugation and possibly taking a negative, has the form
\[
H_t=\begin{pmatrix}t&\sqrt{1-t^2}\\\sqrt{1-t^2}&-t\end{pmatrix},\qquad 0\le t\le1.
\]
For \(\pm I\), the output norm is \(1\). The two eigenvalues of \(L_q(H_t)\) show that
\[
\|L_q(H_t)\|_\infty=\frac{t+\sqrt{4q^2+(1-4q^2)t^2}}2=:g_q(t).
\]
For \(q^2\le1/2\), the derivative \(g_q'(t)\) is nonnegative on \([0,1]\), so its maximum is \(g_q(1)=1\). For \(q^2>1/2\), the unique maximum is at
\[
t_q=\frac1{\sqrt{4q^2-1}}\in(0,1),
\quad g_q(t_q)=\frac{2q^2}{\sqrt{4q^2-1}}.
\]
Indeed \(g_q'(t)=\tfrac12[1+(1-4q^2)t/\sqrt{4q^2+(1-4q^2)t^2}]\), and its sign is positive to the left of \(t_q\) and negative to the right when \(q^2>1/2\). Convexity bounds all Hermitian contractions, while \(H_1\) or \(H_{t_q}\) attains the bound. The stated sharp \(\infty\)-norm profile follows.

**3. Sharp trace-norm profile.** The real trace pairing \(\operatorname{tr}(GH)\) identifies the dual of the Hermitian operator-norm space with the Hermitian trace-norm space. Moreover \(L_q\) is self-adjoint under that pairing: \(\operatorname{tr}(G L_q(H))=\operatorname{tr}(L_q(G)H)\). Therefore \(\|L_q\|_{1\to1}=\|L_q\|_{\infty\to\infty}\). For an explicit trace-norm extremizer, let \(v=(\sqrt r,\sqrt{1-r})^{\mathsf T}\) and \(H=vv^*\), with \(r=1\) when \(q^2\le1/2\) and \(r=2q^2/(4q^2-1)\in(0,1)\) otherwise. Then \(\|H\|_1=1\) and
\[
\|L_q(H)\|_1=\sqrt{r^2+4q^2r(1-r)}=K(q).
\]
This also proves sharpness directly over real symmetric perturbations.

**4. The transition in the original eigenvalues.** The second branch exceeds one exactly for \(q>1/\sqrt2\), since its square differs from one by \((2q^2-1)^2/(4q^2-1)\). The equivalent inequality \(a/(a+b)>1/\sqrt2\) rearranges to \(a/b>1+\sqrt2\). Thus the transition is both necessary and sufficient; in particular, a simple nonzero spectral gap does **not** by itself guarantee local nonexpansion in \(S_1\) or \(S_\infty\).

**5. Passage from local to global sharp constants.** Fix arbitrary \(A,B\in\mathcal H_2\) and put \(A_t=A+t(B-A)\), \(0\le t\le1\). If \(\det(A_t)\) is not the zero polynomial, it vanishes for only finitely many values of \(t\). Between those values the function \(t\mapsto F(A_t)\) is continuously differentiable. On strictly positive definite segments its derivative is the identity, on strictly negative definite segments it is zero, and on indefinite segments Steps 1–3 give bounds \(\|DF(A_t)\|_{1,\infty}\le\sup_{0<q<1}K(q)=2/\sqrt3\) and \(\|DF(A_t)\|_{2\to2}\le1\). Integrating on each subinterval and using continuity through singular times gives the corresponding pairwise Lipschitz inequalities.

If instead \(\det(A_t)\equiv0\), every \(A_t\) has rank at most one. Thus \(F(A_t)=A_t\) where \(\operatorname{tr}A_t\ge0\), and \(F(A_t)=0\) where \(\operatorname{tr}A_t\le0\). The trace is affine in \(t\), so there is at most one sign-switch and each piece is \(1\)-Lipschitz along the segment. The same global inequalities follow.

For sharpness, take \(A_\epsilon=\operatorname{diag}(1,-\epsilon)\) with \(\epsilon>0\), so \(q=1/(1+\epsilon)\uparrow1\). For each fixed \(\epsilon\) take \(B=A_\epsilon+\delta H\), where \(H=H_{t_q}\) for the operator norm or \(H=vv^*\) from Step 3 for the trace norm. As \(\delta\downarrow0\), the ratio \(\|F(B)-F(A_\epsilon)\|_p/\|B-A_\epsilon\|_p\) approaches \(K(q)\); then \(\epsilon\downarrow0\) gives \(2/\sqrt3\). For \(S_2\), take any two distinct positive definite scalar matrices to attain ratio one. This completes both global sharp constants and the local classification. \(\square\)

## Verification
Execute `python3 check.py` with Python 3 and only its standard library. The checker reconstructs each \(2\times2\) positive part from eigenvalues, compares the closed local profile with dense samples of Hermitian symmetries, tests explicit operator-norm and trace-norm extremizers, checks Fréchet linearization at strictly indefinite matrices, and stress-tests pairwise bounds in all three norms. It is independent of externally installed computational mathematics libraries. These finite tests do not prove maximality, sharpness for all parameters, or the global statement; Steps 1–5 do.

## Relationship to prior work
The operator-functional-calculus setting and distinction between scalar and operator Lipschitz estimates are classical; see Aleksandrov–Peller [1] and Bhatia [2]. Caspers–Potapov–Sukochev–Zanin [4] prove weak-type bounds for absolute-value differences in general operator ideals; their estimates do not yield the displayed exact two-eigenvalue local threshold. Levene [3] computed the sharp \(2/\sqrt3\) norm for a two-by-two **idempotent** triangular Schur multiplier, which corresponds to the *endpoint* matrix of the present derivative family as \(q\uparrow1\). Accordingly, the global sharp constant alone is **not** an independent novelty claim. The genuine refined statement is the exact *non-idempotent* continuum \(L_q\) arising from the positive-part derivative, including a nonexpansive phase and its exact eigenvalue-ratio frontier. General variational and factorization formulas for Schur multiplier norms, such as Christensen [5], apply in principle to this small matrix family but do not evaluate its parameter dependence or express the clipping transition. The present calculation explicitly solves the associated extremum for every \(q\), rather than asserting that generic multiplier theory was absent. Published results on other Schur masks, including positive-cone triangular truncation in dimension three [6], do not control these spectral derivatives in dimension two.

## Limitations
The profile is for Hermitian \(2\times2\) matrices only, at strictly indefinite invertible points for differentiability; no claim is made for nonsmooth derivatives at matrices with zero eigenvalues, larger dimensions, non-Hermitian inputs, or other Schatten exponents. The threshold is a sharp quantitative finite-dimensional invariant, not a claim about arbitrary-dimensional positive-part maps. A general Schur-multiplier factorization theory encompasses the underlying optimization problem, and equivalent explicit formulas under different parametrizations may exist in historical matrix-analysis literature. Novelty has been assessed against specified relevant sources but has not been independently established.

## References
[1] A. B. Aleksandrov and V. V. Peller, *Operator Hölder–Zygmund functions*, arXiv:0907.3049, initial public preprint 2009-07-17; *Advances in Mathematics* 224 (2010), 910–966.

[2] R. Bhatia, *Modulus of continuity of the matrix absolute value*, *Indian Journal of Pure and Applied Mathematics* 41 (2010), 99–111. DOI: 10.1007/s13226-010-0014-0.

[3] R. H. Levene, *Norms of idempotent Schur multipliers*, arXiv:1302.4849, initial public preprint 2013-02-20; *New York Journal of Mathematics* 20 (2014), 325–352, particularly Proposition 5.1 on small masks; primary MSC 47A30.

[4] M. Caspers, D. Potapov, F. Sukochev and D. Zanin, *Weak type estimates for the absolute value mapping*, arXiv:1309.3378, initial public preprint 2013-09-13; *Journal of Operator Theory* 73 (2015), 361–384.

[5] E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670v1 (2025), especially Theorems 1.2, 1.3, and 1.6 on general multiplier-norm factorizations.

[6] *Sharp positivity-restricted triangular truncation in dimension three*, publicly indexed mathematical note, 2026; concerns a different mask acting on positive-semidefinite input and not the spectral positive-part derivative.
