# Sharp forward-depth costs of eliminating one-step past on bounded cycles

## Finding

Let \(S\subset\mathbb N_{>0}\) be a finite nonempty set. On the class \(\mathcal C_S\) of **all finite disjoint unions of directed cycles whose lengths belong to \(S\)**, the least modal depth of any positive forward-only formula equivalent at every world to the one-step-past formula \(\mathbf Pp\) is
\[
D_+(S)=\max_{r,s\in S}\operatorname{lcm}(r,s)-1.
\]
Consequently, when \(S=\{1,\ldots,n\}\) and \(n\ge2\), the least positive depth is \(n(n-1)-1\); when \(n=1\) it is \(0\).

For the same consecutive length sets, when Boolean negation is permitted, the **exact** least depth is
\[
D_{\mathrm B}(n)=\begin{cases}0,&n=1,\\2n-3,&n\ge2.\end{cases}
\]
Thus removal of a one-step past operator requires **quadratic forward depth without negation**, even though linear depth suffices and is optimal with Boolean negation.

## Assumptions and scope

A directed cycle of length \(r\ge1\) has vertices \(\mathbb Z/r\mathbb Z\) with the unique forward edge \(i\to i+1\). A model is an arbitrary finite disjoint union of these frames with an arbitrary assignment of truth values to the propositional letter \(p\) at each vertex. The future diamond \(\mathbf F\varphi\) means that \(\varphi\) holds at the **unique immediate successor**; the past diamond \(\mathbf P\varphi\) uses the converse edge, hence the unique immediate predecessor. In particular, \(\mathbf F\) here is **not** the transitive-closure/eventually operator of linear-time temporal logic.

The positive language has \(p,\top,\bot,\wedge,\vee,\mathbf F\), with no negation. The Boolean language additionally allows \(\neg\) and arbitrary Boolean truth functions. In both languages, the modal depth of an atom or constant is \(0\), the depth of a Boolean combination is the maximum of its subformula depths, and applying \(\mathbf F\) increases depth by \(1\). Extra propositional letters would not reduce any lower bound because their valuations may all be fixed constants. A defining formula must work **uniformly** for every frame in the class, every valuation and every root. The results also apply to elimination of \(\mathbf P\psi\) for any substituted formula \(\psi\), by uniform substitution into the displayed definitions.

## Proof

**Forward-prefix locality.** At a point of an \(r\)-cycle, write \(a_i\in\{0,1\}\) for the truth value of \(p\) at the \(i\)-th successor, so \(a_{i+r}=a_i\). A forward-only formula of depth at most \(d\) depends only on \(a_0,\ldots,a_d\), by induction on the syntax. For the positive language it is also monotone in the coordinatewise order on these prefix bits. The desired past truth value is \(a_{r-1}\).

**Positive upper bound.** Set \(L=\max_{r,s\in S}\operatorname{lcm}(r,s)\). The following positive formula has depth exactly at most \(L-1\):
\[
\Phi_S^+(p)=\bigvee_{r\in S}\ \bigwedge_{s\in S}
  \mathbf F^{\operatorname{lcm}(r,s)-1}p.
\]
At an actual cycle of length \(t\in S\), if the preceding vertex satisfies \(p\), choose the disjunct indexed by \(r=t\); every exponent \(\operatorname{lcm}(t,s)-1\) is congruent to \(-1\) modulo \(t\), so this disjunct is true. Conversely, if the preceding vertex does not satisfy \(p\), then in *every* disjunct indexed by \(r\), choose the conjunct indexed by \(s=t\); its exponent is again congruent to \(-1\) modulo \(t\), so that disjunct is false. Thus \(\Phi_S^+(p)\leftrightarrow\mathbf Pp\) on \(\mathcal C_S\).

**Positive lower bound.** Choose \(r,s\in S\) with \(\operatorname{lcm}(r,s)=L\). On an \(r\)-cycle take the valuation \(u_i=1\) exactly when \(i\equiv-1\pmod r\); on an \(s\)-cycle take \(v_i=0\) exactly when \(i\equiv-1\pmod s\), and \(v_i=1\) otherwise. At the two roots, \(\mathbf Pp\) is respectively true and false. However,
\[
u_i\le v_i\qquad(0\le i\le L-2),
\]
because simultaneous congruences \(i\equiv-1\pmod r\) and \(i\equiv-1\pmod s\) first occur at \(i=L-1\). By prefix locality and monotonicity, a positive formula of depth at most \(L-2\) cannot be true on the first model and false on the second. When \(L=1\), the upper bound \(0\) is automatically minimal. This proves \(D_+(S)=L-1\). For consecutive lengths with \(n\ge2\), every least common multiple of two lengths at most \(n\) is at most \(n(n-1)\): equal lengths yield at most \(n\), and distinct lengths have product at most \(n(n-1)\). Equality is attained by the coprime pair \(n,n-1\).

**Boolean upper bound.** Assume \(n\ge2\). Let \(m=2n-2\). If two infinite binary successor traces have respective periods \(r,s\le n\) and agree on the first \(m\) positions, then their common prefix is a word having both periods \(r\) and \(s\). Since
\[
m\ge r+s-\gcd(r,s),
\]
the classical Fine–Wilf periodicity theorem shows that the common prefix has period \(\gcd(r,s)\). As \(m\ge\max(r,s)\), the two predecessors have the respective values at prefix positions \(r-1\) and \(s-1\); both coincide with the value at the residue \(-1\) modulo \(\gcd(r,s)\). Thus the past truth value is determined by precisely the first \(m\) forward bits. An explicit future-only Boolean defining formula is the finite disjunction, over all realizable binary prefixes \(w=(w_0,\ldots,w_{m-1})\) whose uniquely determined predecessor bit is \(1\), of
\[
\bigwedge_{i=0}^{m-1}
\begin{cases}
\mathbf F^ip,&w_i=1,\\
\neg\mathbf F^ip,&w_i=0.
\end{cases}
\]
Its depth is at most \(m-1=2n-3\). The formula uses only the fixed integer \(n\), not a model or a valuation.

**Boolean lower bound.** On an \(n\)-cycle use the repeated binary block \(u=(1^{n-2}01)^\omega\); on an \((n-1)\)-cycle use \(v=(1^{n-2}0)^\omega\). Their prefixes coincide at indices \(0\le i\le2n-4\): the first \(n-1\) symbols are \(1^{n-2}0\), followed in both traces by \(n-2\) ones. But their predecessor bits differ, since the final bit of the first period is \(1\) and of the second is \(0\). Prefix locality therefore excludes every Boolean forward formula of depth \(2n-4\) or less. For \(n=2\) the first block is \(01\) and the second is \(0\); the same argument applies. For \(n=1\) predecessor equals the current vertex and \(p\) itself is depth \(0\).

## Verification

The standalone standard-library script `verify.py` enumerates every binary valuation of cycles of each length up to \(7\). It checks that a Boolean prefix of the claimed length determines the predecessor but one fewer bit does not, and checks the exact positive threshold by comparing all true/false predecessor valuation pairs under coordinatewise prefix order. It independently evaluates \(\Phi_S^+\) for every valuation on every nonempty subset of lengths up to \(6\), plus the consecutive sets through \(7\); it checks the explicit lower-bound witnesses. Running `python3 verify.py` ends with:

```
VERIFY_OK sets=127 valuations=5828
```

These are *finite* replay checks; the proofs for all finite sets \(S\) and arbitrarily large cycles use the symbolic arguments above, not finite enumeration.

## Relationship to prior work

Figallo, Sarmiento and Pezzini study the algebraic and proof-theoretic semantics of the future/past tense operators and establish completeness for the minimal tense logic. The present result asks a different restricted-frame question: what exact future nesting depth is required to eliminate one immediate-past operator on finite permutation frames? The source paper does not give these depth thresholds.

Kurtonina and de Rijke characterize positive modal definability through directed simulations (including bounded-degree simulation methods). Their general characterization does not provide the exact least depth for this particular class, whereas the cyclic witnesses and least-common-multiple normal form here give a numerical classification. Dvorkin addresses positive definability and interpolation in various modal logics, without bounded-cycle predecessor-depth calculations. Fine and Wilf's theorem supplies the classical periodic-prefix upper-bound ingredient; it does not itself state a result about modal expressibility or the sharp positive-depth obstruction. The restricted-class and uniform-formula quantifiers matter: general tense frames need not admit any such forward-only elimination.

## Limitations

The theorem concerns the immediate-successor relation of finite permutation frames, not arbitrary functional, transitive, branching, or infinite frames. The Boolean exact optimum is proved for consecutive length sets; the exact positive optimum holds for any finite nonempty length set. Formula **depth**, not minimal formula size, is optimized. The result does not assert that the standard Fine–Wilf lemma or the general simulation-preservation principle is new. Mathematical correctness is supported by a complete proof and finite checks; no independent audit or expert validation is asserted.

## References

1. Martín Figallo, Jonathan Sarmiento and Luis Pezzini, *Tense Logic via Truth Degrees: An Algebraic Completeness Result for Kashima's Calculus*, arXiv:2610.01547v1 (first public 2026-10-01), https://arxiv.org/html/2610.01547v1 .
2. Natasha Kurtonina and Maarten de Rijke, *Simulating without Negation*, Journal of Logic and Computation 7 (1997), 501–522, doi:10.1093/logcom/7.4.501, https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/kurtonina-simulating-1997.pdf .
3. Lev Dvorkin, *Monotonicity versus positivity in modal logics*, arXiv:2602.02837v2 (2026), https://arxiv.org/html/2602.02837v2 .
4. N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, Proceedings of the American Mathematical Society 16 (1965), 109–114, doi:10.1090/S0002-9939-1965-0174934-9 .
5. Rikuya Hamai, Yuto Nakashima and Shunsuke Inenaga, *The Parameterized Periodicity Lemma*, arXiv:2608.21912 (2026), https://arxiv.org/abs/2608.21912 (recounts the classical Fine–Wilf threshold).
