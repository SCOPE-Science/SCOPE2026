# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Write
\[
C=AX-XB,\qquad D_k=A^kX-XB^k.
\]
Direct expansion gives
\[
A^nC=D_{n+1}-D_nB,\qquad
CB^n=D_{n+1}-AD_n.
\]
Thus both terms on the left lie in \(S_p\).

The key interpolation step was checked separately. If \(T\) is subnormal and
\(T^nY\in S_p\), take a normal extension \(N\). Spectral truncation away from zero
makes the family \(|N|^{nz}Y\) a standard strip interpolation family. Interpolation
between \(S_\infty\) and \(S_p\) at \(1/n\), followed by removal of the spectral cutoff, gives
\[
\|TY\|_{np}\le \|T^nY\|_p^{1/n}\|Y\|^{1-1/n}.
\]
This argument works for rectangular Schatten operators as needed for the extension-space inclusion.

Applying the lemma to \(A,C\) gives \(AC\in S_{np}\). Since subnormal operators are
hyponormal, \(AA^*\le A^*A\); Douglas factorization therefore gives
\(A^*=R_A^*A\) for a contraction \(R_A\), so \(A^*C\in S_{np}\).
Applying the lemma to \(B^*,C^*\) gives \(CB\in S_{np}\). Hyponormality of \(B^*\)
gives \(B^*B\le BB^*\), hence \(B^*=BR_B\) for a contraction \(R_B\), and
\(CB^*\in S_{np}\).

The cubic identity
\[
CC^*C=CX^*A^*C-CB^*X^*C
\]
then gives \(CC^*C\in S_{np}\). For \(C=V|C|\),
\[
CC^*C=V|C|^3,
\]
so
\[
\|CC^*C\|_{np}=\|C\|_{3np}^3.
\]
This establishes the upper bound.

For the lower barrier, taking \(B=\omega A\) with a nontrivial \(n\)-th root of unity
and \(A=\operatorname{diag}(j^{-1/q})\) makes the \(n\)-th defect zero and the
\((n+1)\)-st defect an \(S_p\) operator whenever \(q<(n+1)p\), while the first defect
is not in \(S_q\). All operators in this example are normal. Hence no hidden
complementability, compactness, duality, or inheritance assertion enters the obstruction.

The general-ideal refinement was also checked against the earlier proof: once
\(A^*C,CB^*\in I^{1/2^{n-1}}\), the displayed cubic identity already places
\(CC^*C\) in that ideal. Polar decomposition permits a cube root immediately; the
two extra square-root steps used in the earlier estimate are unnecessary for this conclusion.

## Originality

**PASS, to the best of our knowledge.** Kittaneh's 1986 primary result proves the
subnormal \(n=2\) conclusion \(C\in S_{8p}\). Kittaneh's 2006 Theorem 1 treats
consecutive powers under range-inclusion hypotheses and concludes
\(C\in S_{2^{n+1}p}\); its proof explicitly contains the intermediate fact
\[
CC^*C\in I^{1/2^{n-1}}.
\]
The present cube-root refinement extracts the stronger consequence of that intermediate
fact, while the subnormal normal-extension argument improves the full dependence to
\(S_{3np}\).

Duggal's 2001 work treats coprime powers with semi-Fredholm or near-isometric
hypotheses. Bhatia--Kittaneh 1997 obtains stronger Schatten consequences in special
self-adjoint and positive settings; those cases are prior art and are not part of the
novelty claim.

No equivalent linear-in-\(n\) conclusion for the general subnormal consecutive-power
setting was located in the literature compared with these results. The residual
originality risk is not zero: older work on commutants modulo ideals, subnormal
operators, interpolation of symmetric ideals, or Fuglede-type theorems may contain
an equivalent sharpening under different notation.

## Value

**PASS.** The main improvement is asymptotic rather than a one-parameter adjustment:
the previously stated Schatten exponent \(2^{n+1}p\) is replaced, in the classical
subnormal setting, by \(3np\). The normal diagonal obstruction proves that the
optimal universal exponent must be at least \((n+1)p\), so the growth order is
settled as linear and the remaining constant-factor gap is below three.

The arbitrary-ideal cube-root observation is independently reusable: whenever the
earlier range-inclusion descent produces the cubic defect in a root ideal, one can
stop at that cubic power rather than perform two more square-root extractions.

## Scientific limitations

The optimal exponent is not determined: the proved interval is
\[
(n+1)p\le q_{\mathrm{opt}}(n,p)\le3np.
\]
The linear proof depends on subnormality through a normal extension. Under only
the range-inclusion assumptions, the available conclusion is
\(I^{1/(3\cdot2^{n-1})}\), not the linear Schatten bound.

The stated interpolation argument assumes \(1\le p<\infty\). The compact-ideal
endpoint is qualitative and already lies within the earlier ideal theorem.
Originality remains to the best of our knowledge, with differently formulated older
commutant-modulo-ideal and symmetric-ideal literature the principal residual risk.
