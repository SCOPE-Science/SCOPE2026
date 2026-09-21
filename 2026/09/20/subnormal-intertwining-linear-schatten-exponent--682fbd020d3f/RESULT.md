# Linear Schatten exponent for consecutive-power intertwinings

## Result

Let \(H\) be a separable complex Hilbert space, let \(n\ge2\) and \(1\le p<\infty\), and let
\(A,B,X\in B(H)\). Assume that \(A\) and \(B^*\) are subnormal. Put
\[
D_k=A^kX-XB^k,\qquad C=AX-XB.
\]
If
\[
D_n,D_{n+1}\in S_p,
\]
then
\[
\boxed{C\in S_{3np}.}
\]

Thus the Schatten exponent in the consecutive-power intertwining theorem grows at most linearly in \(n\). Kittaneh's general theorem gives \(C\in S_{2^{n+1}p}\) under the weaker range assumptions
\(\overline{\operatorname{ran}A}\subseteq\overline{\operatorname{ran}A^*}\) and
\(\overline{\operatorname{ran}B^*}\subseteq\overline{\operatorname{ran}B}\). In the original subnormal case \(n=2\), the conclusion improves from \(S_{8p}\) to \(S_{6p}\).

A quantitative form is
\[
\|C\|_{3np}^3
\le
\|X\|\,\|C\|^{\,2-1/n}
\left[
\bigl(\|D_{n+1}\|_p+\|B\|\,\|D_n\|_p\bigr)^{1/n}
+
\bigl(\|D_{n+1}\|_p+\|A\|\,\|D_n\|_p\bigr)^{1/n}
\right].
\]

There is also a general ideal refinement of Kittaneh's proof. Under only the two range-inclusion hypotheses above, if \(I\) is a two-sided ideal and
\[
D_n,D_{n+1}\in I,
\]
then
\[
\boxed{
C\in \left(I^{1/2^{\,n-1}}\right)^{1/3}
      = I^{1/(3\cdot 2^{\,n-1})}.
}
\]
For \(I=S_p\), this yields \(C\in S_{3\cdot2^{n-1}p}\), already improving the previously stated \(S_{2^{n+1}p}\) conclusion without strengthening the hypotheses.

## Subnormal interpolation lemma

The new linear bound comes from the following elementary lemma.

**Lemma.** If \(T\) is subnormal, \(Y\) is bounded between Hilbert spaces, and
\[
T^nY\in S_p,\qquad n\ge2,\quad 1\le p<\infty,
\]
then
\[
TY\in S_{np}
\]
and
\[
\|TY\|_{np}\le
\|T^nY\|_p^{1/n}\|Y\|^{1-1/n}.
\]

**Proof.** Let \(N\) be a normal extension of \(T\), and view \(Y\) as taking values in the invariant copy of the original Hilbert space inside the extension space. Write
\(N=U|N|\). Normality makes \(U\) commute with \(|N|\), hence
\[
\||N|^nY\|_p=\|N^nY\|_p,\qquad
\||N|Y\|_{np}=\|NY\|_{np}.
\]

For a spectral cutoff \(P_\varepsilon=\mathbf 1_{[\varepsilon,\|N\|]}(|N|)\),
the strip family
\[
F_\varepsilon(z)=|N|^{nz}P_\varepsilon Y,\qquad 0\le\Re z\le1,
\]
is bounded and analytic. On the two boundary lines,
\[
\|F_\varepsilon(it)\|\le\|Y\|,
\qquad
\|F_\varepsilon(1+it)\|_p
\le\||N|^nY\|_p.
\]
Complex interpolation between \(S_\infty\) and \(S_p\), at \(\theta=1/n\), gives
\[
\||N|P_\varepsilon Y\|_{np}
\le
\||N|^nY\|_p^{1/n}\|Y\|^{1-1/n}.
\]
Letting \(\varepsilon\downarrow0\) and using lower semicontinuity of Schatten norms gives the lemma. \(\square\)

## Proof of the main estimate

Simple algebra gives
\[
A^nC=D_{n+1}-D_nB,\qquad
CB^n=D_{n+1}-AD_n.
\]
Hence both \(A^nC\) and \(CB^n\) lie in \(S_p\).

Apply the lemma to \(A\) and \(C\):
\[
AC\in S_{np},\qquad
\|AC\|_{np}\le
\|A^nC\|_p^{1/n}\|C\|^{1-1/n}.
\]
Since a subnormal operator is hyponormal,
\[
AA^*\le A^*A.
\]
Douglas factorization therefore gives a contraction \(R_A\) such that
\(A=A^*R_A\), equivalently \(A^*=R_A^*A\). Thus
\[
A^*C\in S_{np}
\]
with the same upper bound.

Taking adjoints of \(CB^n\in S_p\) gives
\[
B^{*n}C^*\in S_p.
\]
Because \(B^*\) is subnormal, the lemma gives \(B^*C^*\in S_{np}\), hence
\(CB\in S_{np}\). Hyponormality of \(B^*\) gives
\[
B^*B\le BB^*,
\]
so Douglas factorization yields a contraction \(R_B\) with \(B^*=BR_B\). Consequently
\[
CB^*=CBR_B\in S_{np}.
\]

Now use
\[
C^*=X^*A^*-B^*X^*
\]
to obtain
\[
CC^*C
=
CX^*A^*C-CB^*X^*C
\in S_{np}.
\]
If \(C=V|C|\) is its polar decomposition, then
\[
CC^*C=V|C|^3.
\]
Therefore
\[
\|CC^*C\|_{np}=\|C\|_{3np}^3,
\]
which proves \(C\in S_{3np}\). Inserting the two interpolation estimates and
\[
\|A^nC\|_p\le\|D_{n+1}\|_p+\|B\|\,\|D_n\|_p,
\qquad
\|CB^n\|_p\le\|D_{n+1}\|_p+\|A\|\,\|D_n\|_p
\]
gives the displayed quantitative inequality.

## General ideal refinement

Kittaneh's range-inclusion argument yields, from \(D_n,D_{n+1}\in I\),
\[
A^*C,\ CB^*\in I^{1/2^{\,n-1}}.
\]
The same cubic identity therefore gives
\[
CC^*C\in I^{1/2^{\,n-1}}.
\]
Writing \(CC^*C=V|C|^3\), two-sidedness and self-adjointness of the ideal imply
\[
|C|^3\in I^{1/2^{\,n-1}},
\]
hence
\[
C\in \left(I^{1/2^{\,n-1}}\right)^{1/3}.
\]
This stops the root extraction at the cubic expression already present in the earlier proof.

## A linear lower barrier

The order \(n\) cannot be removed from any universal Schatten exponent, even for normal diagonal operators.

Fix \(q<(n+1)p\), choose a nontrivial \(n\)-th root of unity \(\omega\), and on
\(\ell_2(\mathbb N)\) set
\[
A=\operatorname{diag}(j^{-1/q})_{j\ge1},
\qquad B=\omega A,\qquad X=I.
\]
Both \(A\) and \(B^*\) are normal. Since \(\omega^n=1\),
\[
D_n=A^n-B^n=0,
\]
whereas
\[
D_{n+1}=(1-\omega)A^{n+1}\in S_p
\]
because \((n+1)p/q>1\). But
\[
C=A-B=(1-\omega)A\notin S_q
\]
because \(\sum_{j\ge1}j^{-1}=\infty\).

Consequently, if \(r_n p\) denotes any universal Schatten exponent that could replace the conclusion above, then necessarily
\[
(n+1)p\le r_n p\le 3np.
\]
In particular, the correct growth order in \(n\) is linear, not exponential, although the optimal constant remains open.

## Relation to prior work

Kittaneh (1986) proved the \(n=2\) subnormal statement with conclusion \(S_{8p}\). Duggal (2001) extended related commutant-modulo-\(S_p\) results to coprime powers under additional hypotheses. Kittaneh (2006) proved the consecutive-power theorem for arbitrary two-sided ideals under range-inclusion hypotheses and, for \(I=S_p\), obtained \(S_{2^{n+1}p}\).

Bhatia and Kittaneh (1997) obtained sharper conclusions for special self-adjoint and positive settings through operator-monotone-function and unitarily invariant norm inequalities. Those structurally stronger cases are prior art and are not included in the novelty claim here.

The contribution claimed here is the linear \(S_{3np}\) conclusion for the general subnormal consecutive-power setting, the explicit \((n+1)p\) lower barrier showing that linear growth is unavoidable, and the cube-root refinement of the arbitrary-ideal argument.

## Originality and limitations

Originality is asserted only to the best of our knowledge. No equivalent linear-in-\(n\) Schatten conclusion was located in the literature compared with the 1986, 2001, and 2006 commutant/intertwining results. The main residual risk is that an equivalent interpolation sharpening may occur under different notation in older commutant-modulo-ideal, subnormal-operator, or symmetric-ideal literature.

The result does not determine the optimal exponent between \((n+1)p\) and \(3np\). The \(S_{3np}\) proof uses subnormality essentially through normal extensions; under the weaker range-inclusion assumptions it gives only the cube-root refinement stated above. The interpolation proof is stated for \(1\le p<\infty\); the compact-ideal endpoint is a different qualitative statement already covered by the earlier ideal theorem.

## References

1. F. Kittaneh, *On the commutants modulo \(C_p\) of \(A^2\) and \(A^3\)*, J. Austral. Math. Soc. Ser. A **41** (1986), 47--50. https://doi.org/10.1017/S1446788700028056
2. B. P. Duggal, *The commutant modulo \(C_p\) of co-prime powers of operators on a Hilbert space*, J. Math. Anal. Appl. **263** (2001), 110--120. https://doi.org/10.1006/jmaa.2001.7601
3. F. Kittaneh, *Some intertwining relations modulo operator ideals*, Glasgow Math. J. **48** (2006), 111--117. https://doi.org/10.1017/S0017089505002910
4. R. Bhatia and F. Kittaneh, *Some inequalities for norms of commutators*, SIAM J. Matrix Anal. Appl. **18** (1997), 258--263. https://doi.org/10.1137/S0895479895293235
