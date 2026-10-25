# Exact finite-ring holonomy census for nonabelian group cellular automata

## Finding
Let \(S\) be any nonabelian finite simple group and \(m\geq1\). Consider an arbitrary surjective one-dimensional group cellular automaton over \(S^m\). The established factor-permutation normal form allows us to write it, after fixed coordinate identifications, as
\[
(Fx)_{n,\pi(j)}=\phi_j(x_{n+v_j,j}),\qquad n\in\mathbb Z,\quad 0\leq j<m,
\]
where \(\pi\in\mathfrak S_m\), \(v_j\in\mathbb Z\), and \(\phi_j\in\operatorname{Aut}(S)\). Let \(F_N\) be its restriction to configurations periodic in space with period dividing \(N\geq1\). For every cycle \(C=(j_0,\ldots,j_{\ell-1})\) of \(\pi\), indexed so that \(\pi(j_r)=j_{r+1}\) cyclically, define
\[
V_C=\sum_{j\in C}v_j,\quad H_C=\phi_{j_{\ell-1}}\circ\cdots\circ\phi_{j_0},\quad
g_C=\gcd(N,V_C),\quad L_C=\frac{\ell N}{g_C},\quad d_C(t)=\gcd(t,L_C).
\]
The convention is \(\gcd(N,0)=N\). Different starting indices conjugate \(H_C\) inside \(\operatorname{Aut}(S)\), so the fixed-element counts below do not depend on that choice.

**Exact finite-volume periodic-point census.** For every integer \(N\geq1\) and time \(t\geq1\),
\[
\boxed{\#\operatorname{Fix}(F_N^t)=\prod_{C\in\operatorname{Cyc}(\pi)}
\left|\operatorname{Fix}_S\left(H_C^{(N/g_C)(t/d_C(t))}\right)\right|^{g_Cd_C(t)}.}
\]
Consequently the number \(P_N(t)\) of points with *least* temporal period \(t\), and the number of corresponding primitive periodic orbits, are explicitly
\[
P_N(t)=\sum_{d\mid t}\mu(t/d)\#\operatorname{Fix}(F_N^d),\qquad
\operatorname{Orb}_N(t)=P_N(t)/t.
\]
Thus the formula determines the complete temporal cycle distribution of the finite-ring permutation \(F_N\), and hence its Artin–Mazur dynamical zeta function.

**Sharp finite-ring untwisting criterion.** Let \(U_N\) be the permutation of the same finite configuration set with identical \(\pi,v_j\) but with every \(\phi_j\) replaced by the identity. Then the following are equivalent:
\[
F_N\text{ is conjugate to }U_N\text{ as a finite dynamical system}
\quad\Longleftrightarrow\quad
H_C^{N/g_C}=\operatorname{id}_S\text{ for every }C.
\]
This is an equivalence under unrestricted finite-set conjugacy, not merely under coordinatewise gauge changes.

When every \(V_C\ne0\), the *bi-infinite* temporal system \(F\) is nevertheless topologically conjugate to a full two-sided shift with alphabet \(S^B\), where \(B=\sum_C|V_C|\). The conjugacy is as a temporal dynamical system and need not commute with spatial shifts. Thus the finite-ring holonomies can obstruct a conjugacy which exists in infinite volume.

For instance, let \(S=A_5\), \(m=1\), \(v_0=1\), and let \(\phi_0\) be conjugation of \(A_5\) by the transposition \((1\ 2)\in S_5\). Then the infinite system is a full shift on 60 symbols, whereas
\[
\#\operatorname{Fix}(F_N)=\begin{cases}6,&N\text{ odd},\\60,&N\text{ even}.
\end{cases}
\]
The finite-ring system is conjugate to the untwisted cyclic shift precisely for even \(N\).

## Assumptions and scope
The finite group \(S\) is nonabelian simple; its automorphisms are group automorphisms, not merely bijections. The normal form applies to surjective group cellular automata over \(S^m\) by the published factor-permutation structure, with any number of permutation cycles allowed. The asserted fixed-point formula also holds, by its proof, for an arbitrary finite group \(S\) whenever the displayed monomial-automorphism normal form is directly assumed. Only periodic spatial boundary conditions are considered in the finite-volume statements. \(\operatorname{Fix}_S(\psi)=\{s\in S:\psi(s)=s\}\). All powers of maps mean composition, with negative spatial shifts permitted.

## Proof
**1. Decomposition of the coordinate permutation.** On \(I_N=(\mathbb Z/N\mathbb Z)\times\{0,\dots,m-1\}\), each output index \((n,\pi(j))\) reads the unique input index \((n+v_j,j)\). Thus there is a permutation \(P_N\) of \(I_N\) and one automorphism label for each arrow. On a \(\pi\)-cycle \(C\) of length \(\ell\), following the input arrows for \(\ell\) steps returns to the same internal index and advances the spatial index by \(V_C\) modulo \(N\). Translation by \(V_C\) on the cyclic group of order \(N\) has exactly \(g_C=\gcd(N,V_C)\) orbits, each of length \(N/g_C\). Hence the full index permutation \(P_N\) has exactly \(g_C\) orbits arising from \(C\), and every such orbit has length \(L_C=\ell N/g_C\).

**2. Monodromy along an index orbit.** Along a complete \(P_N\)-orbit associated with \(C\), the automorphisms compose to a cyclic conjugate of \(H_C^{N/g_C}\). Indeed, every block of \(\ell\) arrows passes through the internal factors in the same cyclic order; their composition is a cyclic conjugate of \(H_C\), and the number of full rounds is \(N/g_C\). Conjugation of the automorphism does not change the number of its fixed elements. For a cyclically weighted permutation of length \(L\) with return automorphism \(M\), its \(t\)-th power partitions that orbit into \(d=\gcd(L,t)\) cycles of length \(L/d\). Along each such cycle of the \(t\)-th power the composed return map is a conjugate of \(M^{t/d}\): each traverses exactly \(t/d\) complete rounds of the original weighted orbit. A fixed configuration of the \(t\)-th power is specified by choosing, independently on each of those \(d\) cycles, one element of \(\operatorname{Fix}_S(M^{t/d})\), then propagating it by the invertible arrow labels. Thus that original index orbit contributes \(|\operatorname{Fix}_S(M^{t/d})|^d\) configurations.

**3. Exact count and primitive cycles.** Inserting \(L=L_C\) and \(M=H_C^{N/g_C}\), then multiplying over the \(g_C\) disjoint index orbits for each internal cycle \(C\), gives the boxed product. All sites and internal factors are covered exactly once, so there are no compatibility constraints between choices on different orbits. Because every arrow automorphism is invertible, \(F_N\) permutes the finite set \(S^{mN}\). The identity \(\#\operatorname{Fix}(F_N^t)=\sum_{d\mid t}P_N(d)\) and Möbius inversion give the least-period and orbit formulas without any assumption of a uniform orbit length.

**4. The finite-ring obstruction is necessary and sufficient.** Setting \(t=1\) in the count gives
\[
\#\operatorname{Fix}(F_N)=\prod_C|\operatorname{Fix}_S(H_C^{N/g_C})|^{g_C},\qquad
\#\operatorname{Fix}(U_N)=|S|^{\sum_Cg_C}.
\]
If \(F_N\) and \(U_N\) are conjugate, these numbers agree. Every factor on the left is at most its corresponding factor on the right, and equality for a finite group automorphism occurs exactly when the automorphism is the identity on all elements. Therefore each \(H_C^{N/g_C}\) must be the identity. Conversely, when all these holonomies are trivial, choose an arbitrary base coordinate on each full \(P_N\)-orbit and recursively transport a coordinatewise automorphism gauge around that orbit so that all weighted arrows become identity arrows. Closing the recursion is consistent precisely because the complete-orbit holonomy is trivial. The product of the gauges is a bijective conjugacy from \(F_N\) to \(U_N\).

**5. Infinite volume.** For a nonzero \(V_C\), following the analogous coordinate permutation on \(\mathbb Z\times C\) has exactly \(|V_C|\) bi-infinite orbits (each step along the internal cycle moves the site by \(V_C\)); there are no finite index orbits. Choose a base index on each such orbit, label its coordinates by \(\mathbb Z\), and transport gauge automorphisms along the two infinite directions. No closure/holonomy condition exists. The resulting coordinatewise homeomorphism conjugates the temporal action to the ordinary shift on one independent bi-infinite \(S\)-sequence per index orbit. Grouping the \(B\) sequences yields a full shift on \(S^B\). Product topology ensures continuity of coordinate permutations and of the coordinatewise automorphism gauge, even though this is not required to be a sliding-block code for the original spatial shift.

**6. The alternating-group example.** Conjugation by \((1\ 2)\) has order two as an automorphism of \(A_5\), and its fixed subgroup is the centralizer of \((1\ 2)\) inside \(A_5\), of order six. In the single-factor unit-shift example \(g_C=1\) and \(L_C=N\), so the one-step fixed count is \(|\operatorname{Fix}_{A_5}(\phi_0^N)|\), which equals six for odd \(N\) and sixty for even \(N\). The sharp untwisting condition becomes \(\phi_0^N=\operatorname{id}\), equivalent to even \(N\).

## Verification
An exact finite-group checker separately implements \(A_5\) as the 60 even permutations on five letters. It explicitly follows spatial-index orbits and composes the actual conjugation automorphisms; it then compares every resulting fixed-point count to the closed formula using \(\gcd\)-data and internal-cycle holonomies. It passed 1,320 parameter combinations and 11 additional odd/even twisted-shift checks, including time powers beyond the one-step case. Run `python checker.py` using the packaged source; the captured output is in `checker_output.txt`. Enumeration confirms tested finite cases only, while Steps 1–6 establish the unrestricted theorem for every finite size and time.

## Relationship to prior work
Castronuovo, Dennunzio and Margara's 2025 paper establishes the nonabelian-simple-factor permutation normal form, powers that become spatial shifts, transitivity criteria, and entropy formulas. Their Theorem 10 and structural discussion in Section 6 are the starting point here, not claimed as new. The 2026 transitivity paper extends that analysis to higher dimensions and explains the factor-permutation reduction (its Section 6). The present calculation adds the **entire finite-spatial-ring fixed-time profile**, the resulting primitive-period census, and a necessary-and-sufficient holonomy criterion for finite-volume untwisting; merely knowing a power of the infinite automaton is a spatial shift does not specify the fixed counts at all intermediate times. Existing general literature on periodic boundary conditions motivates this comparison, but may contain more abstract cycle-index formulations, which remain a historical-priority risk.

## Limitations
The group-cellular-automaton classification concerns surjective rules over powers of one nonabelian finite simple group; it does not treat nonsurjective rules or general extensions between distinct simple groups. The infinite full-shift conjugacy requires every spatial drift \(V_C\ne0\). Its conjugacy is temporal, not necessarily equivariant under the original spatial shift. Nothing here claims that the elementary cyclic-orbit counting mechanism is new as a general principle for weighted permutations; historical overlap with general permutation or graph-covering holonomy theory has not been exhaustively excluded. The result does not characterize arbitrary finite-boundary dynamics outside periodic spatial boundary conditions.

## References
1. N. Castronuovo, A. Dennunzio, and L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics*, arXiv:2507.09761v1 (first public July 13, 2025), especially Section 6 and Theorem 10. https://arxiv.org/pdf/2507.09761
2. N. Castronuovo, A. Dennunzio, and L. Margara, *Topological transitivity of group cellular automata is decidable*, arXiv:2601.16243v1 (first public January 22, 2026), especially Section 6. https://arxiv.org/html/2601.16243v1
3. A. Dennunzio, E. Formenti, and L. Margara, *On the Dynamical Behavior of Cellular Automata on Finite Groups*, IEEE Access 12 (2024), 122061–122077, DOI:10.1109/ACCESS.2024.3452199 (broader context only).
