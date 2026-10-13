# A weighted-tableau census and universal quarter-law for continuous Alexandrov relations

## Finding

Fix positive integers \(r,m\). Let \(C_s=\{0,1,\ldots,s-1\}\), with the Alexandrov topology of upward-closed subsets. For any binary relation \(R\subseteq C_r\times C_m\), let \(R_x=\{y:xRy\}\). Its modal predicate transformers are
\[
 \Box_R U=\{x:R_x\subseteq U\},\qquad
 \Diamond_R U=\{x:R_x\cap U\ne\varnothing\}.
\]
Call \(R\) *two-sided continuous* when both transformers send every open subset of \(C_m\) to an open subset of \(C_r\). When \(r=m\), this is ordinary upper- and lower-semicontinuity of a relational space.

**Enumeration theorem.** Such an \(R\) either has every successor row empty, or has every row nonempty. In the nonempty case its row minima \(a_i\) and maxima \(b_i\), indexed by \(0\le i<r\), obey
\[
 0\le a_0\le\cdots\le a_{r-1}<m,\qquad
 0\le b_0\le\cdots\le b_{r-1}<m,\qquad a_i\le b_i.
\]
Conversely every such pair of sequences gives precisely \(\prod_{i=0}^{r-1}2^{\max\{b_i-a_i-1,0\}}\) two-sided continuous relations. Thus their total number is
\[
 N_{r,m}=1+\sum_{\substack{0\le a_0\le\cdots\le a_{r-1}<m\\0\le b_0\le\cdots\le b_{r-1}<m\\a_i\le b_i\ \mathrm{for\ all}\ i}}
 \prod_{i=0}^{r-1}2^{\max\{b_i-a_i-1,0\}}.
\]
This is a weighted two-row semistandard-tableau count. The unweighted subfamily whose nonempty rows are intervals has the *closed* count
\[
 N^{\mathrm{int}}_{r,m}=1+\frac{1}{r+1}\binom{r+m-1}{m-1}\binom{r+m}{m}.
\]
For each *fixed* \(m\ge3\), put
\[
 C_m=\prod_{j=0}^{m-2}\left(1-\frac{2^{\max\{j-1,0\}}}{2^{m-2}}\right)^{-2},\qquad M=\frac{m(m+1)}2.
\]
Then, as \(r\to\infty\),
\[
 N_{r,m}=C_m\,2^{(m-2)r}+O_m\!\left(r^M 2^{(m-3)r}\right),
 \qquad \frac{N_{r,m}}{2^{rm}}\sim C_m\,4^{-r}.
\]
The exponential decay base \(1/4\) for the probability that a uniformly random relation is two-sided continuous is independent of the fixed target size \(m\ge3\). At \(m=1\), \(N_{r,1}=2\); at \(m=2\), \(N_{r,2}=1+\binom{r+2}{2}\). For self-relations the first five counts \(N_{n,n}\) are \(2,7,80,2855,374660\).

## Assumptions and scope

Both carrier sets are finite, nonempty **chains** with the upward Alexandrov topology. The relation is arbitrary: no reflexivity, transitivity, symmetry, interval-valuedness or seriality is presupposed. Every open set, including the empty and total set, must be preserved by **both** raw box and diamond transformers. The rectangular case \(r\ne m\) uses two-sorted predicate transformers, and the diagonal case \(r=m\) is the usual relational-space modal semantics. The notation \(O_m(\cdot)\) allows constants depending on the fixed integer \(m\).

## Proof

**1. Endpoint test and seriality dichotomy.** Every open subset of \(C_m\) is \(U_t=\{t,t+1,\ldots,m-1\}\) for exactly one \(0\le t\le m\). For an empty row set \(a(x)=m\) and \(b(x)=-1\); otherwise set \(a(x)=\min R_x\), \(b(x)=\max R_x\). For every \(t\),
\[
 x\in\Box_R U_t\iff a(x)\ge t,
 \qquad x\in\Diamond_R U_t\iff b(x)\ge t.
\]
A subset of \(C_r\) is open iff its indicator is nondecreasing along the chain. Therefore both transformers preserve opens iff both \(a(x)\) and \(b(x)\) are nondecreasing with \(x\). An empty row followed by a nonempty row violates monotonicity of \(a\), whereas a nonempty row followed by an empty row violates monotonicity of \(b\); hence all rows have the same emptiness status. The all-empty relation qualifies. For nonempty rows, monotonicity becomes the displayed inequalities, with \(a_i\le b_i\).

**2. Weights and tableaux.** Given distinct endpoints \(a_i<b_i\), the row contains both and may contain or omit any of its \(b_i-a_i-1\) interior points. Equal endpoints force a singleton. All these choices are independent and do not change any modal-open test in step 1; multiplying weights and summing over endpoint sequences proves the count. Restricting every row to the complete integer interval leaves one row for each endpoint pair. Map the endpoint sequences to a two-row semistandard Young tableau of shape \((r,r)\) by putting \(a_i+1\) in the upper row and \(b_i+2\) in the lower row of column \(i\). The two rows are weakly increasing, the columns strictly increasing, and all entries lie in \(\{1,\ldots,m+1\}\). Conversely these conditions uniquely reconstruct \(0\le a_i\le b_i<m\). The classical hook-content (equivalently Weyl dimension) formula gives
\[
 \#\mathrm{SSYT}_{(r,r)}(m+1)
 =\prod_{j=3}^{m+1}\frac{r+j-1}{j-1}\frac{r+j-2}{j-2}
 =\frac{1}{r+1}\binom{r+m}{m}\binom{r+m-1}{m-1}.
\]
Adding the all-empty relation yields the second formula. When \(m=1\), there is exactly one nonempty row type, so the total is two. When \(m=2\), the three nonempty row types are totally ordered by endpoints and each has unit weight, giving \(1+\binom{r+2}{2}\).

**3. Rational generating function and sharp asymptotic.** Let \(P_m=\{(a,b):0\le a\le b<m\}\), ordered coordinatewise, and set \(w(a,b)=2^{\max\{b-a-1,0\}}\). Let \(B_{r,m}=N_{r,m}-1\), with the empty-sequence convention \(B_{0,m}=1\). A weighted weak multichain is uniquely a strict chain \(q_1<\cdots<q_k\) with a positive multiplicity for every \(q_i\). Thus the rational generating function is
\[
 H_m(z):=\sum_{r\ge0}B_{r,m}z^r
 =\sum_{\substack{Q\text{ a strict chain}\\\text{in }P_m}}
 \prod_{q\in Q}\frac{w(q)z}{1-w(q)z},
\]
where the empty chain contributes one. For \(m\ge3\), the unique maximum weight is \(w_*=2^{m-2}\), attained at \(q_*=(0,m-1)\). Every other weight is at most \(w_*/2\). The interval endpoints preceding \(q_*\) are exactly \((0,j)\) with \(0\le j<m-1\); those succeeding it are exactly \((a,m-1)\) with \(1\le a<m\). Each of these two families is totally ordered and every left element precedes every right element. Therefore the contribution of strict chains containing \(q_*\) factors *exactly* as
\[
 \frac{w_*z}{1-w_*z}
 \prod_{j=0}^{m-2}\left(1-w(0,j)z\right)^{-1}
 \prod_{a=1}^{m-1}\left(1-w(a,m-1)z\right)^{-1}.
\]
Chains omitting \(q_*\) have generating functions whose poles are all at reciprocals of weights no greater than \(w_*/2\). Taking the coefficient of the unique dominant pole \((1-w_*z)^{-1}\) gives
\[
 C_m=\prod_{j=0}^{m-2}(1-w(0,j)/w_*)^{-1}
 \prod_{a=1}^{m-1}(1-w(a,m-1)/w_*)^{-1}.
\]
The two lists of weights coincide and equal \(2^{\max\{j-1,0\}}\), giving the stated product. Rational-function partial fractions bound all other coefficients by \(O_m(r^M (w_*/2)^r)\), where \(M=|P_m|\), and the extra all-empty relation contributes only one. Dividing by the exact \(2^{rm}\) unrestricted relations proves the universal quarter-law.

## Verification

Run `python3 artifacts/verify.py` with the Python standard library. The checker independently evaluates all modal-open conditions and the endpoint monotonicity condition for each of **74,954** relations on all pairs \((r,m)\) with \(1\le r,m\le4\). It finds **3,958** continuous relations and **960** whose rows are all empty or all intervals; both totals agree pair-by-pair with the displayed formulas. It independently checks fixed-target asymptotic constants through \(m=6\) against exact weighted counts at \(r=80\). The diagonal census from the weighted formula through size five is \(2,7,80,2855,374660\). These finite tests do not establish the theorem for unbounded \(r,m\); the three proof steps do.

## Relationship to prior work

Collinson's 2026 *Topological Dualities for Modal Algebras* motivates continuity of relational spaces via simultaneous openness of box and diamond inverse-image operators. Barmak–Mrozek–Wanner's 2018 Lemma 3.2 supplies more general finite-poset semicontinuity characterizations; the endpoint condition here is an elementary chain specialization of known structural theory, **not** claimed as new by itself. Walker (1984) and Roddy–Schröder (2005) previously study isotone relations, mainly for fixed-point problems. The hook-content formula is classical and the interval-valued subcount is an application, not a newly discovered tableau identity. The proposed contribution is the integrated **unrestricted weighted census and its exact fixed-target asymptotic** for the modal-continuity class, including the distinguished diagonal counts and exponential constant. The available relevant primary texts do not report that combined enumeration.

## Limitations

This is an enumerative theorem for finite **chains**, not an axiomatization, duality theorem, or characterization for arbitrary posets or infinite relational spaces. The asymptotic holds with \(m\) fixed and at least three; no joint \(r,m\to\infty\) estimate is asserted. For arbitrary noninterval rows, no hook-product closed form is claimed; the exact weighted sum and transfer recurrence are given instead. Prior isotone-relation literature is extensive, and an older equivalent enumeration may exist, particularly in material not available in full text. No independent mathematical audit has been performed.

## References

1. M. Collinson, *Topological Dualities for Modal Algebras*, arXiv:2604.20603v1 (first submitted 2026-04-22), §§1–2. https://arxiv.org/abs/2604.20603.
2. J. A. Barmak, M. Mrozek, T. Wanner, *A Lefschetz Fixed Point Theorem for Multivalued Maps of Finite Spaces*, arXiv:1808.08985 (2018), §§3,7, especially Lemma 3.2. https://arxiv.org/abs/1808.08985.
3. J. W. Walker, *Isotone relations and the fixed point property for posets*, Discrete Mathematics 48 (1984), 275–288, DOI 10.1016/0012-365X(84)90188-2.
4. M. S. Roddy, B. S. W. Schröder, *Isotone relations revisited*, Discrete Mathematics 290 (2005), 229–248.
5. Standard hook-content enumeration of semistandard Young tableaux, as recorded in the FindStat Semistandard Tableaux collection. https://www.findstat.org/CollectionsDatabase/SemistandardTableaux/.
