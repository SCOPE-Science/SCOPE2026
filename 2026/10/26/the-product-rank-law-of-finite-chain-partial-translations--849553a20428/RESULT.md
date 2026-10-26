# The product-rank law of finite-chain partial translations

## Finding
Let \(X_n=\{1,\ldots,n\}\), and let \(S_n\) be the inverse monoid of all partial order-preserving isometries of \(X_n\), including the empty map. Composition is evaluated from left to right: \((fg)(x)=g(f(x))\). For every integer \(n\ge1\) define the ordered-product rank polynomial
\[
G_n(t)=\sum_{(f,g)\in S_n^2}t^{|\operatorname{dom}(fg)|}.
\]
Put \(X=3+t\). The following is an exact identity in \(\mathbb Z[t]\):
\[
\boxed{G_n(t)=X^n+\sum_{j=1}^{n-1}\left(2^{j+1}(j+3)-6\right)X^{n-j}+(4-8n)2^n+4n^2+8n-4.}
\]
In particular, for \(1\le r\le n\), the number of ordered pairs with product rank \(r\) is
\[
\boxed{[t^r]G_n(t)=\binom nr3^{n-r}+\sum_{j=1}^{n-r}\left(2^{j+1}(j+3)-6\right)\binom{n-j}{r}3^{n-j-r}.}
\]
The rank-zero count is \(G_n(0)\); the complete profile therefore follows from a single sum. For \(n\ge2\), exactly \(3n+10\) pairs have product rank \(n-1\), and exactly one pair has product rank \(n\).

If \(F_n,G_n\) are independent uniform elements of \(S_n\), and \(R_n=|\operatorname{dom}(F_nG_n)|\), then
\[
\boxed{d_{\mathrm{TV}}\!\left(\mathcal L(R_n),\operatorname{Bin}(n,1/4)\right)=O(n^{-1/2}),}\qquad
\boxed{\mathbb E R_n=\frac n4-\frac{16}{27}+O(n^2 2^{-n}).}
\]
Consequently \((R_n-n/4)/\sqrt{3n/16}\) converges in distribution to a standard normal random variable. The quantitative approximation and the nonzero constant bias concern *independent uniform factors*, not a uniform product element or conditional commuting factors.

## Assumptions and scope
The distance is the ordinary integer distance on \(X_n\). Each nonempty element of \(S_n\) is uniquely a restriction of a translation \(x\mapsto x+a\), with \(a\in\{1-n,\ldots,n-1\}\). The eligible source interval is
\[
I_a=\{x\in X_n:x+a\in X_n\},\qquad |I_a|=n-|a|.
\]
Every nonempty subset of \(I_a\) specifies one distinct element. The empty restriction is common to all \(2n-1\) translations, but constitutes just one element of \(S_n\). Hence
\[
|S_n|=1+\sum_{a=1-n}^{n-1}(2^{n-|a|}-1)=3\cdot2^n-2(n+1).
\]
The theorem is valid also at \(n=1\), when \(G_1(t)=3+t\). The polynomial counts ordered pairs, so a zero product contributes to the coefficient at \(t^0\) whether or not either factor is zero.

## Proof
**Translation pair enumeration.** Temporarily distinguish every formal empty restriction by its translation label \(a\). The labeled family has
\[
Z_n=\sum_{a=1-n}^{n-1}2^{n-|a|}=3\cdot2^n-4
\]
members, counting the empty map \(h_n=2n-1\) times. For labeled translations with shifts \(a,b\), the source points able to survive the composition are exactly
\[
T_{a,b}=\{x\in X_n:x,\ x+a,\ x+a+b\in X_n\}.
\]
This is an interval of length
\[
L_{a,b}=\max\{0,n-w(a,b)\},\qquad
w(a,b)=\max(0,a,a+b)-\min(0,a,a+b).
\]
Choose source subsets for both factors independently. At each of the \(L_{a,b}\) common eligible positions, the four possible pairs of binary membership choices contribute \(3+t\): precisely the simultaneous membership choice survives. The other membership choices are free. Thus the labeled product polynomial at fixed shifts is exactly
\[
2^{2n-|a|-|b|-2L_{a,b}}(3+t)^{L_{a,b}}.
\]
The exponent is nonnegative because the two eligible intervals intersect in \(L_{a,b}\) positions. Summing gives a finite double-shift representation of the labeled polynomial.

**Collapse to one sum.** Write \(X=3+t\). Separate shifts by sign. The shift pair \((0,0)\) contributes \(X^n\). Pairs with exactly one zero shift and the other of magnitude \(j\ge1\) contribute \(4\cdot2^jX^{n-j}\). Pairs with both shifts nonzero and of the same sign, whose magnitudes add to \(j<n\), contribute \(2(j-1)2^jX^{n-j}\). For pairs with opposite nonzero signs, grouping by \(j=\max(|a|,|b|)\) gives \(2(2^{j+1}-3)X^{n-j}\); indeed the inner weight for the smaller magnitude is \(1+2\sum_{u=1}^{j-1}2^{j-u}=2^{j+1}-3\). These three contributions total \((2^{j+1}(j+3)-6)X^{n-j}\) for every \(1\le j<n\).

Same-sign nonzero pairs whose magnitude sum is at least \(n\) have no common eligible source point. Their rank-zero contribution is
\[
2\sum_{k=2}^n(k-1)2^k=(n-2)2^{n+2}+8,
\]
where the identity also holds for \(n=1\) by the empty-sum convention. This completes the labeled polynomial.

**Removing redundant zeros.** Set \(c_n=h_n-1=2n-2\) and \(N_n=|S_n|\). Passing from the actual monoid to the labeled multiset adds \(c_n\) copies of the zero transformation. The additional \(2c_nN_n+c_n^2\) ordered products all have rank zero. Subtracting this constant from the labeled polynomial gives the stated formula for \(G_n\), since
\[
(n-2)2^{n+2}+8-2c_nN_n-c_n^2=(4-8n)2^n+4n^2+8n-4.
\]
The coefficient formula follows by binomial expansion. The top two coefficients are \(1\) and \(3n+10\), respectively.

**Binomial approximation.** In the labeled probability model, a shift \(A_n\) has probability proportional to \(2^{-|a|}\), and conditional on its shift every eligible source point is selected independently with probability \(1/2\). The shifts of two independent labeled factors are independent. Conditional on \(A_n=a,B_n=b\), their product rank is therefore *exactly* \(\operatorname{Bin}(L_{a,b},1/4)\).

The shifts \(A_n,B_n\) converge to independent two-sided geometric variables \(A,B\) with
\[
\Pr(A=k)=\frac{2^{-|k|}}3,\qquad k\in\mathbb Z.
\]
Here \(W_n=n-L_{A_n,B_n}=\min\{n,w(A_n,B_n)\}\) has uniformly bounded expectation, since \(w(a,b)\le |a|+|b|\) and \(\sup_n\mathbb E|A_n|\le4/3\). Let \(p=1/4\). Adding one Bernoulli variable to \(\operatorname{Bin}(m,p)\) changes its law by total variation at most \(p\max_j\Pr(\operatorname{Bin}(m,p)=j)\). The binomial maximum point mass is \(O((m+1)^{-1/2})\), by elementary Stirling bounds. On \(W_n\le n/2\), adding the \(W_n\) missing trials therefore costs \(O(W_n/\sqrt n)\); on the complementary event the cost is at most one, and Markov's inequality bounds its probability by \(O(n^{-1})\). The labeled rank law is thus within \(O(n^{-1/2})\) of \(\operatorname{Bin}(n,1/4)\).

The total variation distance between a uniform actual element and the projection of a uniform labeled element is \(O(n2^{-n})\): only the probability assigned to the zero map changes. For two independent factors, their product-rank laws differ in total variation by at most twice that amount. This proves the stated approximation, and the central limit assertion follows from the binomial central limit theorem.

**Mean and constant bias.** The identity
\[
w(a,b)=\frac{|a|+|b|+|a+b|}{2}
\]
holds for real \(a,b\). The geometric sums give \(\mathbb E|A|=4/3\), and convolution yields
\[
\Pr(A+B=k)=\frac{(3|k|+5)2^{-|k|}}{27},\qquad
\mathbb E|A+B|=\frac{56}{27}.
\]
Therefore \(\mathbb Ew(A,B)=64/27\). Geometric tails, together with \(w(a,b)\le |a|+|b|\), show
\[
\mathbb E\min\{n,w(A_n,B_n)\}=\frac{64}{27}+O(n2^{-n}).
\]
The labeled mean product rank equals \(\frac14(n-64/27)+O(n2^{-n})\). Every redundant zero label contributes zero rank, so the actual mean is obtained by multiplying the labeled mean by \((Z_n/N_n)^2=1+O(n2^{-n})\). The resulting error is \(O(n^2 2^{-n})\), giving \(\mathbb E R_n=n/4-16/27+O(n^22^{-n})\).

## Verification
The standalone program `verify_product_rank.py` uses only the Python standard library. It independently constructs every actual partial translation and directly counts each ordered product rank for \(1\le n\le7\). It compares this with (i) the compact formula and (ii) a separate double-displacement formula. For \(8\le n\le40\), it compares both formulas and checks total ordered-pair counts. It also checks the exact geometric limiting moments and the mean-bias approximation at selected sizes. Run `python verify_product_rank.py`; successful execution prints `VERIFY_OK_PARTIAL_TRANSLATION_PRODUCT_RANK`.

The rank profiles at sizes \(n=1,2,3,4\) are respectively \((3,1)\), \((19,16,1)\), \((115,121,19,1)\), and \((571,672,178,22,1)\), listed from rank zero upward. These finite checks corroborate, but cannot replace, the arbitrary-size combinatorial argument and asymptotic proof.

## Relationship to prior work
Kehinde and Umar (arXiv:1101.0049v1, 30 December 2010) establish the structure, Green relations, and single-element cardinality of finite-chain partial-isometry semigroups; their Sections 2–3 do not give the two-factor multiplication-rank law. Al-Kharousi, Kehinde and Umar (Australasian Journal of Combinatorics 58(3), 2014, 365–375) enumerate single-element height, fixed points, and \(\mathscr D\)-classes; the inspected Sections 2–3 likewise do not state a product-rank convolution or its asymptotics. The known identity \(|S_n|=3\cdot2^n-2(n+1)\) is background, not a new claim.

Other rank-refined multiplication results for commuting idempotents or square-zero partial injections involve different restrictions on the factors and cannot imply the unrestricted independent product law here by substituting parameters. The finite sum here uses the extra metric-translation structure of this particular monoid; a rank profile of arbitrary partial bijections does not itself isolate this monoid. Searches did not identify an equivalent statement, but absence from the inspected literature or an index is not a proof of universal priority.

## Limitations
Only order-preserving distance-preserving partial injections on a finite linear chain are considered. The result does not cover all partial isometries (including order-reversing maps), arbitrary inverse subsemigroups, conditional commuting pairs, or the distribution of individual product outputs. The asymptotic approximation is for the rank random variable, not for the full random product map. The finite verifier is not an infinite proof. Historical equivalents in uninspected literature remain a residual risk, and no independent mathematical validation has been performed.

## References
1. R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049v1, first version 30 December 2010, especially Sections 1–3. https://arxiv.org/abs/1101.0049
2. F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain*, Australasian Journal of Combinatorics **58** (2014), no. 3, 365–375, especially Sections 2–3. https://ajc.maths.uq.edu.au/pdf/58/ajc_v58_p365.pdf
3. F. Al-Kharousi, R. Kehinde and A. Umar, *On the Semigroup of Partial Isometries of a Finite Chain*, Communications in Algebra **44** (2016), no. 2, 639–647, DOI:10.1080/00927872.2014.984838. (Publication record and abstract consulted; 2010 preprint provides accessible primary full text.)
