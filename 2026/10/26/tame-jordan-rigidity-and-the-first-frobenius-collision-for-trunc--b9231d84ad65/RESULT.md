# Tame Jordan rigidity and the first Frobenius collision for truncated Nottingham actions

## Finding
Let \(k\) be a field of characteristic \(p>0\), let \(m\ge3\), and let \(A_m=k[t]/(t^m)\). For a nonidentity normalized substitution automorphism
\[
\phi(t)=t+a_{d+1}t^{d+1}+\cdots+a_{m-1}t^{m-1},\qquad a_{d+1}\ne0,\quad 1\le d\le m-2,
\]
write \(N_\phi=\phi-\operatorname{id}_{A_m}\) for the induced nilpotent \(k\)-linear operator. The integer \(d\) is the first nonlinear depth.

**Tame-depth Jordan rigidity.** If \(m\le p+d\), then for every integer \(j\ge1\)
\[
\operatorname{rank}(N_\phi^j)=\max\{m-1-jd,0\}.
\]
Consequently, as a \(k\)-linear operator, \(\phi\) has one unipotent singleton block from the constants, together with \(d\) unipotent Jordan blocks of lengths
\[
\lambda_i=1+\left\lfloor\frac{m-1-i}{d}\right\rfloor,
\qquad 1\le i\le d.
\]
In particular, the full linear similarity class depends only on the first nonlinear depth, not on any later coefficient. Its fixed subalgebra is \(k\oplus t^{m-d}A_m\).

**Sharp first Frobenius step.** At the immediately subsequent truncation \(m=p+d+1\), the full rank profile changes universally to
\[
\operatorname{rank}(N_\phi^j)=\max\{p-1-(j-1)d,0\}
\qquad(j\ge1).
\]
Its Jordan type consists of two singleton blocks and \(d\) blocks of lengths
\[
\mu_i=1+\left\lfloor\frac{p+d-1-i}{d}\right\rfloor,
\qquad1\le i\le d.
\]
Moreover, \(A_m^\phi=k\oplus t^pA_m\). The tame rank prediction is too large by exactly one whenever it is positive; hence \(m=p+d\) is the largest uniform truncation bound for the tame-depth formula at each depth \(d\).

**First-wild similarity collision.** At \(m=p+d+1\), choose any substitutions \(\phi\) and \(\psi\) of respective first nonlinear depths \(d\) and \(d+1\). Their natural linear representations on \(A_m\) are similar if and only if \(d\ge p-1\). Thus the first wild step sometimes collapses two different ramification depths into one modular Jordan class; for \(d\le p-2\), their second nilpotent-power ranks distinguish them.

If \(k=\mathbb F_q\), the depth-\(d\) stratum has exactly \((q-1)q^{m-d-2}\) elements. In the complete short-truncation range \(3\le m\le p+1\), these \(m-2\) depth strata give pairwise distinct natural-module similarity classes, and the identity is the sole additional class. For a uniformly chosen normalized substitution, the probability that its fixed space has dimension \(r\) is
\[
\Pr(\dim_k A_m^\phi=r)=
\begin{cases}
(q-1)q^{m-r-1}/q^{m-2},&2\le r\le m-1,\\
q^{-(m-2)},&r=m.
\end{cases}
\]
The already-known fixed-subalgebra spectrum in this short range is included for context; the results asserted here concern the entire Jordan profile and its optimal characteristic boundary.

## Assumptions and scope
All fields have prime characteristic \(p\), including characteristic two; algebraically closedness is not assumed. The substitution group is the group of \(k\)-algebra automorphisms \(\phi\) of \(A_m\) satisfying \(\phi(t)\equiv t\pmod{t^2}\). It is the finite truncated quotient of the formal Nottingham substitution group, and acts faithfully on the \(m\)-dimensional \(k\)-space \(A_m\). The depth \(d\) is the least \(j\ge1\) for which the coefficient of \(t^{j+1}\) is nonzero; the identity has no depth and is excluded from depth-dependent formulas. Powers \(N_\phi^j\) are powers of the \(k\)-linear difference operator, not substitution powers of the formal series. Rank formulas hold for every positive integer \(j\), including after the operator becomes zero.

## Proof
Write \(u(t)=\phi(t)-t=a_{d+1}t^{d+1}+O(t^{d+2})\) with \(a_{d+1}\ne0\). By binomial expansion, for every integer \(i\ge1\),
\[
N_\phi(t^i)=i\,a_{d+1}t^{i+d}+O(t^{i+d+1}). \tag{1}
\]
This yields the filtration estimate \(N_\phi(t^iA_m)\subseteq t^{i+d}A_m\). When the displayed coefficient remains nonzero under iteration, induction yields
\[
N_\phi^j(t^i)
=a_{d+1}^{j}\!\left(\prod_{h=0}^{j-1}(i+hd)\right)t^{i+jd}
+O(t^{i+jd+1}). \tag{2}
\]
Suppose \(m\le p+d\). For every potentially nonzero term with \(i+jd\le m-1\), each factor in (2) is a positive integer at most \(m-1-d\le p-1\), hence a nonzero element of \(k\). Therefore the monomials indexed by \(1\le i\le m-1-jd\) have images with distinct, nonzero leading degrees \(i+jd\), while all higher-degree monomials and the constant are killed. This proves \(\operatorname{rank}N_\phi^j=\max(m-1-jd,0)\). The shift sending \(t^i\) to \(t^{i+d}\) on the ideal \(tA_m\), and zero when the degree is out of range, has precisely those ranks. Ranks of all nilpotent powers uniquely determine its Jordan partition; its chains begin in residues \(i=1,\ldots,d\), giving the displayed \(\lambda_i\), with one extra constant singleton.

The same leading-term argument at \(j=1\) gives \(\ker N_\phi=k\oplus t^{m-d}A_m\): the indicated terms are fixed, whereas every nonzero linear combination involving lower-degree monomials has a lowest-degree image term that cannot cancel. This is a subalgebra because it is the fixed ring of an automorphism.

Now assume \(m=p+d+1\). For \(1\le i\le p-1\), equation (1) has a nonzero leading term of degree \(i+d<m\), and the degrees are distinct. For \(i\ge p+1\), the filtration estimate makes \(N_\phi(t^i)=0\). For \(i=p\), Frobenius gives
\[
N_\phi(t^p)=(t+u(t))^p-t^p=u(t)^p\in t^{p(d+1)}A_m=0,
\]
because \(p(d+1)\ge p+d+1=m\). Thus \(N_\phi\) kills the whole ideal \(t^pA_m\), its rank is \(p-1\), and its fixed algebra is precisely \(k\oplus t^pA_m\).

For \(j\ge2\), a monomial \(t^i\) with \(i+(j-1)d\ge p\) is sent by \(N_\phi^{j-1}\) into \(t^pA_m\), hence is killed by the next application. Conversely, if \(1\le i\le p-1-(j-1)d\), each coefficient in (2) is nonzero modulo \(p\), and the final exponent satisfies \(i+jd\le p+d-1<m\), giving independent leading terms. Therefore \(\operatorname{rank}N_\phi^j=\max(p-1-(j-1)d,0)\) for every positive \(j\). These ranks coincide with those of a step-\(d\) shift on a space of dimension \(p+d-1=m-2\), supplemented by two one-dimensional zero summands, proving the \(\mu_i\) partition and the exact one-dimensional loss relative to the tame prediction.

At this same \(m\), a substitution \(\psi\) of depth \(d+1\) is in its tame range, since \(m=p+(d+1)\). Its positive-power ranks are \(\max(p-1-(j-1)(d+1),0)\). If \(d\ge p-1\), both operators have square zero and rank \(p-1\), hence identical Jordan type. If \(d\le p-2\), the wild operator has second-power rank \(p-1-d>0\), while the depth-\(d+1\) operator has second-power rank \(\max(p-2-d,0)\), which is strictly smaller. This proves the if-and-only-if collision statement.

Finally, over \(\mathbb F_q\) there are \(q-1\) choices for the first nonzero coefficient at degree \(d+1\) and \(q^{m-d-2}\) free choices for the remaining coefficients. If \(m\le p+1\), every nonidentity depth satisfies the tame condition, and its fixed-space dimension is \(d+1\). Distinct depths then have distinct ranks of \(N_\phi\) and cannot be linearly similar. Counting the identity separately proves the finite distribution.

## Verification
The standalone program `artifacts/verify.py` constructs the substitution operator directly on \(A_m\) as an \(m\)-by-\(m\) finite-field matrix, raises \(N_\phi\) to every positive power through its dimension, and computes Gaussian-elimination ranks. It does not compute ranks from the displayed formulas. Finite fields \(\mathbb F_4\) and \(\mathbb F_9\) are independently implemented as polynomial quotients. An execution checked 3,487 matrices, including exhaustive full tame groups in characteristics 2, 3, 5; finite-field extensions; entire first-wild depth strata in several cases; and deterministic samples for longer truncations. Ten additional paired checks compared the first-wild and next-depth similarity profiles. The result was `VERIFY_OK 3487 matrix-power profiles; exhaustive runs, deterministic samples, and first-wild similarity collisions`. These checks corroborate, but do not replace, the general proof.

## Relationship to prior work
Byszewski, Cornelissen and Tijsma develop Nottingham-series depth and break sequences in the context of automata and finite-order substitutions. Their inspected introduction, ramification discussion and finite-order constructions do not give the present full natural-module nilpotent-power rank formulas or the sharp linear-similarity collision criterion. A related published calculation determines the socle series and multipermutation level of truncated Nottingham braces; it treats a different action and invariant. D'Alessandro and Szechtman calculate exponents of finite substitution-group quotients; group exponents alone do not determine Jordan partitions of the natural polynomial module. Its full text could not be inspected, so an undiscovered equivalent rank calculation remains a residual risk. Previously established fixed-algebra distributions in low truncations explain the dimension component of the theorem and are not independently claimed here.

## Limitations
The rank profiles apply in the indicated depth-dependent tame range and at its first characteristic boundary only, not to arbitrary higher truncation lengths. Distinct depths outside the tame range can have identical natural-module Jordan forms, as shown by the collision theorem; global similarity classification in all lengths is not claimed. The group-exponent literature does not by itself settle the module-rank question, but a still-uninspected proof appendix could overlap. The computational experiment is finite and no priority beyond inspected sources is asserted.

## References
1. J. Byszewski, G. Cornelissen, D. Tijsma, *Automata and finite order elements in the Nottingham group*, arXiv:2008.04971 (first public version 11 August 2020), subsequently *Journal of Algebra* **602** (2022), 484–554; DOI 10.1016/j.jalgebra.2022.03.019.
2. A. D'Alessandro, F. Szechtman, *Substitution groups of formal power series*, arXiv:2606.11461 (first public version 9 June 2026); exponent classification, full-text-access limitation noted above.
3. *Truncated Nottingham braces attain maximal multipermutation level at every odd prime*, publicly accessible mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-truncated-nottingham-braces-attain-maximal-multipermutation-leve--fdfe4aefbe51.
