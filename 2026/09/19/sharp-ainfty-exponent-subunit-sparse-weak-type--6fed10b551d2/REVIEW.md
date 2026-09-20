# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The lower-bound construction is finite and can be checked exactly. The nested family
\[
\{[0,1),[0,2^{-1}),\dots,[0,2^{-m})\}
\]
is \(1/2\)-sparse. For
\[
\omega_m=1+(2^m-1)\mathbf 1_{[0,2^{-m})},
\qquad
v_m=M_{\mathscr D}\omega_m,
\]
the mixed characteristic is exactly \([\omega_m,v_m]_{A_1}=1\). Dyadic nesting gives an exact piecewise formula for \(v_m\), from which
\[
\|\mathbf1_{[0,1)}\|_{L^1(v_m)}
=
2+\frac m2-\left(1+\frac m2\right)2^{-m}.
\]

The Fujii--Wilson calculation was checked over all dyadic intervals. Intervals disjoint from or contained in the spike have ratio \(1\); every remaining interval is an ancestor \(I_k=[0,2^{-k})\). For these,
\[
\frac{1}{\omega_m(I_k)}
\int_{I_k}M_{\mathscr D}(\mathbf1_{I_k}\omega_m)
=
1+\frac{(m-k)(1-2^{-m})}
{2(2^{-k}+1-2^{-m})}.
\]
This yields \(m/4\le[\omega_m]_{A_\infty}\le m\) for \(m\ge2\).

For \(f_m=\mathbf1_{[0,1)}\), every sparse average is \(1\) on the smallest interval, so the sparse output there is exactly \((m+1)^{1/r}\), while the \(\omega_m\)-mass of that interval is \(1\). Dividing by the exact input norm gives a lower bound at least \((2/3)m^{1/r-1}\). Since the \(A_\infty\) characteristic is comparable with \(m\), this proves the claimed exponent obstruction. No limiting, probabilistic, or numerical assertion is needed for the proof.

Stress tests include the endpoint tendency \(r\uparrow1\): the power obstruction tends to order one and therefore does not conflict with the distinct logarithmic phenomenon at \(r=1\). All weights are positive and locally integrable, and the sparse family is finite.

## Originality

**PASS, to the best of our knowledge.** The directly relevant source is Gonçalves--Lorist, arXiv:2609.20531 (submitted 17 September 2026). Its Theorem B(ii) proves the \(0<r<1\) weak \(L^1\) upper bound with factor \([\omega]_{A_\infty}^{1/r-1}\) and explicitly states that this case is new even in the dyadic setting. The paper separately identifies sharpness for the logarithmic \(r=1\) endpoint and for specific square-function consequences, but no lower example or optimality statement for the new \(0<r<1\) \(A_\infty\) exponent was located in its theorem statement, introduction, or sharpness discussion.

Nieraeth--Stockdale, arXiv:2409.08921 / Potential Analysis 65 (2026), after Corollary C explicitly asked whether the logarithmic factor was necessary when the sparse power is below one. Their discussion notes that the Hytönen--Li result concerns \(p>1\) and does not settle this endpoint. Hytönen--Li, arXiv:1509.00273 / Proc. Amer. Math. Soc. 146 (2018), gives the mixed weak estimate for \(p>1\), including the analogous exponent \((1/r-1/p)_+\), but not the \(p=1\), \(r<1\) endpoint.

Searches using the source identifier, Fujii--Wilson terminology, subunit sparse powers, weak \(L^1\), mixed \(A_1\)--\(A_\infty\), and the exponent \(1/r-1\), as well as the current SCOPE archive under equivalent terminology, did not locate an endpoint sharpness statement equivalent to this theorem. There is a residual risk that a related nested-weight example in older \(p>1\) sparse-operator literature implicitly yields the same endpoint lower bound after a reformulation, or that a contemporaneous observation following the very recent source preprint is not yet indexed. No specifically identified inaccessible source was found that is more likely than this general residual risk to overturn the originality assessment.

## Value

**PASS.** The source theorem resolves whether a logarithmic loss can be removed for \(0<r<1\); the present lower example identifies the exact remaining growth scale and shows that the resulting power cannot be improved. Fixing \([\omega_m,v_m]_{A_1}=1\) isolates the \(A_\infty\) contribution rather than allowing a lower bound to be absorbed into growth of the mixed characteristic. The construction is explicit, finite, one-dimensional, and gives both the exact Fujii--Wilson profile and a direct weak-level lower bound.

## Limitations

The theorem concerns the sparse operator itself and therefore does not automatically transfer as a lower bound to every operator dominated by such a sparse form. It establishes optimal order in the \(A_\infty\) characteristic, not an exact best numerical constant. It does not sharpen the mixed \(A_1\) exponent, treat \(r=1\), or provide new upper estimates. No independent validation, independent audit, or formal proof-assistant verification is asserted.
