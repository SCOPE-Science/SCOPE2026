# Exact recurrent-orbit and minimum-resource laws for integer diffusion on bistars

## Finding

Let \(D_{a,b}\) be the labelled bistar obtained by joining the hubs of two stars, with \(a\ge1\) distinctly labelled leaves incident to the first hub and \(b\ge1\) distinctly labelled leaves incident to the second. Put \(n=a+b+2\). Each vertex holds an integer, and each edge transfers one unit simultaneously from its higher endpoint to its lower endpoint; a tie transfers nothing. Write \(F\) for this sign-gradient diffusion map and \(S\) for the conserved sum of the vertex values. Two states in the same temporal two-cycle are counted as one orbit.

Define \((t)_+=\max\{t,0\}\). The number of primitive two-cycle orbits **modulo uniform translation** is exactly
\[
\begin{aligned}
N_{a,b}={}&(a+b+1)(a+1)^a(b+1)^b\\
&+(a-b+1)_+(a+1)^a(b-1)^b\\
&+(b-a+1)_+(a-1)^a(b+1)^b\\
&+\mathbf1_{a=b}\,a^{2a}.
\end{aligned}
\]
The convention \(0^r=0\) for positive integer \(r\) applies. At **each fixed integer sum** \(S\), an exact residue-class polynomial below counts the distinct primitive orbits. The only fixed state at sum \(S\) is the all-equal state, present precisely when \(n\mid S\). The already-established general diffusion period theorem implies that no other recurrent periods occur.

For the physically nonnegative census, require **both** phases of the two-cycle to have nonnegative entries. The least conserved sum supporting such a primitive orbit is
\[
\min S=\begin{cases}n-2,&a=b,\\n-1,&a\ne b.\end{cases}
\]
At that least sum there is **exactly one** primitive two-cycle. The balanced-hub condition therefore lowers the exact minimum chip requirement by one, even though both hubs retain a positive number of leaves.

To give the full fixed-sum distribution, put \(U_r(z)=\sum_{j=1}^{r}z^j\), \(V_r(z)=\sum_{j=1}^{r}z^{-j}\), and \(U_0=V_0=0\). In the group ring \(\mathbb Z[z,z^{-1}]/(z^n-1)\), define
\[
\mathcal R_{a,b}(z)=\mathbf1_{a=b}U_a(z)^{2a}
+\sum_{\substack{\alpha,\beta\in\{-1,1\}\\A=a+\alpha\ge1,\ B=b-\beta\ge1,\ H=1+a\alpha-b\beta\ge1}}
\left(\sum_{h=1}^{H}z^{(b+1)h}\right)
\left(\sum_{j=1}^{A}z^{\alpha j}\right)^a
\left(\sum_{j=1}^{B}z^{\beta j}\right)^b.
\]
After reducing all exponents modulo \(n\), the coefficient of \(z^{S\bmod n}\) is **exactly the number of primitive two-cycle orbits at total \(S\in\mathbb Z\)**. In particular, the full unrestricted count depends only on \(S\bmod n\); summing its coefficients gives \(N_{a,b}\).

The complete nonnegative two-cycle generating function \(G_{a,b}(z)=\sum_{S\ge0}C^+_{a,b}(S)z^S\) is
\[
\begin{aligned}
(1-z^n)G_{a,b}(z)={}&U_{a+1}(z)^aV_{b+1}(z)^b
\sum_{h=1}^{a+b+1}z^{(b+1)h+n(b+1-h)_+}\\
&+U_{a+1}(z)^aU_{b-1}(z)^b
\sum_{h=1}^{(a-b+1)_+}z^{(b+1)h}\\
&+V_{a-1}(z)^aV_{b+1}(z)^b
\sum_{h=1}^{(b-a+1)_+}z^{(b+1)h+n(b+1-h)}\\
&+\mathbf1_{a=b}U_a(z)^{2a}.
\end{aligned}
\]
Here an empty sum is zero. Although some factors are Laurent polynomials, every displayed product has only nonnegative powers after its displayed prefactor. Thus this is an ordinary nonnegative-coefficient generating function after division by \(1-z^n\).

For illustration, \(N_{1,1}=13\), \(N_{1,2}=72\), \(N_{2,2}=439\), and \(N_{2,3}=3584\). The full orbit-count vectors at conserved totals modulo \(n\), in order \(0,\ldots,n-1\), are respectively \((2,3,5,3)\), \((16,15,13,13,15)\), \((68,71,75,79,75,71)\), and \((530,523,508,496,496,508,523)\).

## Assumptions and scope

The graph is simple and connected; each star has at least one leaf. Both hubs and all leaves are distinguished; permuting unequal labelled leaf values counts a different state and, when appropriate, a different orbit. There is no restriction on integer heights in the unrestricted census, and all vertices update simultaneously. Uniform translations by an integer preserve the dynamics. They are identified only in the number \(N_{a,b}\), **not** when counting configurations/orbits at a specified conserved total. The nonnegative generating function counts a complete temporal orbit only when every entry in both phases is nonnegative; it is not a claim about all transient starting states.

## Proof

**1. Period-two edge reversal.** Orient the edges of any finite simple graph arbitrarily and let \(B\) be the signed vertex-edge incidence matrix with \(B^{\mathsf T}x\) the oriented edge-height differences. Put \(s=\operatorname{sgn}(B^{\mathsf T}x)\), coordinatewise, so that \(F(x)=x-Bs\). For a period-two state \(y=F(x)\), \(F(y)=x\), and \(t=\operatorname{sgn}(B^{\mathsf T}y)\), conservation around the two steps gives \(B(s+t)=0\). Consequently
\[
0=x^{\mathsf T}B(s+t)=\sum_e(B^{\mathsf T}x)_e(s_e+t_e).
\]
Every summand is nonnegative: for a nonzero difference its own sign contributes \(1\), and the opposite-step sign is at least \(-1\). Hence each initially nonzero edge has opposite sign at the next phase. Also
\[
0=y^{\mathsf T}B(s+t)=\sum_e(B^{\mathsf T}y)_e(s_e+t_e).
\]
The already-reversed edges contribute zero, and any initially tied edge contributes the absolute value of its next-phase difference. Thus ties remain tied. Conversely, if every edge sign reverses (ties stay ties), each edge sends back exactly the chip it sent forward; hence \(F^2(x)=x\). This characterization is also consistent with the previously published property-plus criterion [1]; the present proof is included to expose all strict-boundary cases.

**2. Forced leaf synchronization.** Write the hub heights \(u,v\), left leaf heights \(x_i\), and right leaf heights \(y_j\). Their one-step changes are
\[
\Delta u=\sum_i\operatorname{sgn}(x_i-u)+\operatorname{sgn}(v-u),\qquad
\Delta v=\sum_j\operatorname{sgn}(y_j-v)-\operatorname{sgn}(v-u),
\]
with a leaf change equal to minus its incident edge sign. In a primitive two-cycle, a tied leaf-hub edge forces the hub change to be zero by Step 1. But an active leaf-hub edge whose hub change is zero cannot strictly reverse an integer gap of at least one: the leaf moves only one step toward the hub, producing at best equality. Therefore, if one leaf of a hub is tied, all its leaves are tied. This forces the bridge to be tied, then the other hub to have zero change and all its leaves tied, yielding a fixed state. Thus, in a primitive two-cycle, **all pendant edges are active**. Moreover, active leaves above a hub require its change to be strictly positive, while active leaves below require it to be strictly negative. All leaves at the same hub are therefore on the same side of that hub.

**3. Canonical phase with a strict bridge.** Suppose \(v>u\). Exactly one of the two phases of an orbit satisfies this inequality, since the bridge sign must reverse. Uniformly translate to \(u=0\), set \(v=h>0\), and let \(\alpha,\beta\in\{-1,1\}\) be the common signs of the left and right pendant differences. Then
\[
x_i=\alpha d_i,\qquad y_j=h+\beta e_j,\qquad
\Delta u=a\alpha+1,\quad\Delta v=b\beta-1.
\]
The strict reversal of every leaf edge and the bridge is **equivalent** to
\[
1\le d_i\le a+\alpha,\qquad
1\le e_j\le b-\beta,\qquad
1\le h\le1+a\alpha-b\beta.
\]
Whenever an upper bound is below one its class is empty. Conversely, these inequalities force all edge signs to reverse, and Step 1 therefore proves a genuine period-two orbit. The partner phase is
\[
(u',v',x'_i,y'_j)=
\bigl(a\alpha+1,\ h+b\beta-1,\ \alpha(d_i-1),\ h+\beta(e_j-1)\bigr).
\]
The class \((\alpha,\beta)=(-1,1)\) is empty because its bridge upper bound is \(1-a-b<1\). The other three classes contribute, respectively,
\[
(a+b+1)(a+1)^a(b+1)^b,\qquad
(a-b+1)_+(a+1)^a(b-1)^b,\qquad
(b-a+1)_+(a-1)^a(b+1)^b.
\]
These are the first three terms of \(N_{a,b}\).

**4. Tied bridge.** If \(u=v\), sign reversal forces the hub changes to agree. Their common pendant signs give \(a\alpha=b\beta\). Since \(a,b\ge1\), this is possible in a primitive orbit exactly when \(a=b\) and \(\alpha=\beta\). Choose the unique phase with both groups of leaves strictly above their hubs, set both hubs to zero, and assign independently \(1\le d_i,e_j\le a\). This yields exactly \(a^{2a}\) orbits modulo translation. Its partner has hubs both at height \(a\) and each leaf height decreased by one. No states from Steps 3 and 4 overlap. Summation proves \(N_{a,b}\).

**5. Conserved-total residue polynomial.** In the strict-bridge phase at translation-normalized hub \(u=0\), the conserved sum is
\[
S_0=(b+1)h+\alpha\sum_i d_i+\beta\sum_j e_j.
\]
Uniform translation by an arbitrary integer \(c\) changes the total to \(S_0+nc\), and there is exactly one such \(c\) for each prescribed total congruent to \(S_0\pmod n\). The sum for tied bridges is \(\sum_i d_i+\sum_j e_j\). The product of elementary gap polynomials and bridge polynomial therefore proves the stated coefficient formula in the residue group ring. The equal-height fixed configurations are the only fixed points because \(\sum_w x_w(F(x)_w-x_w)=-\sum_{\{u,v\}\in E}|x_u-x_v|\), which vanishes at a fixed point only when all adjacent values coincide.

**6. Both phases nonnegative.** For the canonical strict-bridge phase of Step 3, the smallest nonnegative global translation is \(c=(b+1-h)_+\) for \((\alpha,\beta)=(1,-1)\), is \(c=0\) for \((1,1)\), and is \(c=b+1-h\) for \((-1,-1)\). These follow by taking the minimum over the explicit two-phase heights in Step 3; every other vertex bound is weaker. For tied bridges \(c=0\). Each further translation raises the total by \(n\), giving the four numerators and the denominator \(1-z^n\) in the nonnegative generating function. Among the strict-bridge classes, the minimum total is \(n-1\) in the \((1,-1)\) class, achieved uniquely at \(h=b+1\), all \(d_i=1\), and all \(e_j=b+1\); the other classes, when nonempty, have minima \(a+2b+1\) and \(2a+b+1\). In the tied-bridge class the minimum is \(2a=n-2\), uniquely attained when all pendant gaps are one. Thus the claimed sharp balanced/unbalanced resource threshold, including uniqueness, follows.

## Verification

Run `python3 verify_bistar.py`. The Python-standard-library verifier independently enumerates **all** normalized potential period-two states for eight labelled bistars, using only graph degrees to bound every hub and leaf difference. It then checks both updates directly, orients each orbit canonically, and compares the resulting complete orbit-to-minimum-resource dictionaries with the separate parameter formula. It also compares the closed total, each conserved-sum residue class, and the first nonnegative chip total. The eight cases are \((a,b)=(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2)\), totalling **9,044 distinct canonical primitive orbits**. Output ends with `BISTAR_DIFFUSION_ALL_CHECKS_PASSED`. The degree bounds make this finite enumeration exhaustive for the **tested** graph sizes, not for all parameters. The infinite-family proof is Steps 1–6.

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski [1] introduce the diffusion map, prove eventual periodicity for complete bipartite graphs and stars, and give the necessary-and-sufficient edge-reversal/property-plus criterion for period two. These foundational mechanisms are not claimed new here. The general period-at-most-two theorem of Long and Narayanan [2] supplies the already-known upper bound on all recurrent periods. Neither inspected primary text gives an exact primitive-two-cycle orbit count for labelled bistars, an all-sums residue polynomial, nor the sharp both-phases-nonnegative threshold. The new combinatorial ingredient is the forced synchronization of every pendant edge at both hubs, together with the strict/tied bridge phase split and the exact gap enumerators. The bistar has two nonpendant hubs and is not covered by an exact star or complete-graph census. Search non-detection does not establish historical uniqueness.

## Limitations

The result is restricted to integer-valued synchronous sign-gradient diffusion on **labelled bistars** with at least one leaf at each hub. It does not give attraction-basin sizes, transient-time distributions or analogous formulas for arbitrary trees or complete bipartite graphs. The unrestricted fixed-sum counts permit negative vertex values; the nonnegative generating function imposes nonnegativity on both phases, not necessarily on preperiodic trajectories. Published-result comparisons remain subject to literature-indexing and historical-equivalence risks.

## References

[1] C. Duffy, T. F. Lidbetter, M. E. Messinger, and R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, initial public arXiv posting September 19, 2016, arXiv:1609.05792, https://arxiv.org/abs/1609.05792 . The material compared includes the 2018 open-access revision, sections 2.3, 3.1 and 3.2.

[2] J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, initial public arXiv posting April 13, 2017, arXiv:1704.04295, https://arxiv.org/abs/1704.04295 . The material compared includes Theorem 1.1 and its period-two proof.
