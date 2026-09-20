# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The example is finite and all relevant quantities can be computed directly.

For the nested dyadic chain \(I_j=[0,2^{-j})\), the family
\(\mathcal S_N=\{I_0,\ldots,I_N\}\) is \(1/2\)-sparse. With
\(\omega_N=1+2^N\mathbf1_{I_N}\), dyadic nesting implies that any interval interacting
with the exceptional block \(I_N\) is either contained in it or is an ancestor \(I_j\).
This reduces the Fujii--Wilson characteristic to an explicit finite maximum. Recomputing
the shell integrals gives

\[
\int_{I_j}M_{\mathscr D}(\mathbf1_{I_j}\omega_N)
=
1+2^{-j}+\frac{N-j}{2},
\]

and therefore

\[
[\omega_N]_{A_\infty}
=
\max_j\left(1+\frac{N-j}{2(1+2^{-j})}\right)
\simeq N.
\]

The choice \(v_N=M_{\mathscr D}\omega_N\) gives
\([\omega_N,v_N]_{A_1}=1\) identically and
\(\int v_N=2+N/2\). For \(f=1\), the sparse operator equals
\((N+1)^{1/r}\) on the deepest interval, while that interval has
\(\omega_N\)-mass \(1+2^{-N}\). The resulting norm ratio is
\(\gtrsim N^{1/r-1}\). There are no limiting exchanges, numerical approximations, or
unverified analytic continuations in the argument.

Potential failure modes were checked: intervals not meeting \(I_N\) and intervals inside
\(I_N\) contribute Fujii--Wilson ratio \(1\); ancestors larger than a given \(I_j\) cannot
increase \(M_{\mathscr D}(\mathbf1_{I_j}\omega_N)\); and the weak-level threshold is chosen
strictly below the value on \(I_N\).

## Originality

**PASS, to the best of our knowledge.**

The full accessible text of arXiv:2609.20531v1 was inspected around Theorem B and its
discussion. The paper proves the upper bound

\[
[\omega,v]_{A_1}[\omega]_{A_\infty}^{1/r-1},\qquad 0<r<1,
\]

and explicitly describes this endpoint range as new even in the dyadic setting. Its
adjacent discussion records known sharpness for \(r=1\), for the \(p=r=2\) logarithm,
and for the Rubio de Francia application, but no lower-bound construction establishing
sharpness of the new \(p=1,\ r<1\) \(A_\infty\) exponent was found.

Searches using combinations of “sparse operator”, “weak endpoint”, “\(r<1\)”,
“\(A_\infty\)”, “sharpness”, “\(1/r-1\)”, and the source title/arXiv identifier did not
locate a prior statement matching this two-weight sharpness result. Older papers by
Hytönen--Li and Nieraeth--Stockdale cover neighboring weighted sparse and endpoint
questions, but the former treats \(p>1\) mixed bounds and the latter left the relevant
sublinear endpoint question open, as also reported by Gonçalves--Lorist.

No current SCOPE record matching the source paper, claim family, or equivalent endpoint
sharpness formulation was found before publication.

The main residual risk is recency: arXiv:2609.20531v1 was submitted on 17 September 2026,
so a contemporaneous observation may not yet be indexed. No inaccessible paper was found
whose known title or abstract specifically suggests that it contains this exact
\(p=1,\ 0<r<1\) two-weight sharpness construction.

## Value

**PASS.**

The source theorem resolves an explicit endpoint problem, but an upper estimate alone does
not determine whether the new \(A_\infty\) power is intrinsic. The present example closes
that quantitative question: the exponent \(1/r-1\) cannot be reduced. Moreover, the
construction keeps \([\omega,v]_{A_1}=1\), so the lower bound isolates the
\(A_\infty\) factor rather than trading growth between the two weight characteristics.
This makes the sharpness statement directly interpretable and reusable in endpoint sparse
domination arguments.

## Scope and limitations

The result is a sharpness theorem for the positive sparse model itself. It is not a lower
bound for every concrete singular integral or square function dominated by that model.
It does not determine the best dependence on \(r\), nor does it address the distinct
logarithmic endpoint at \(r=1\).

No independent validation is asserted.
