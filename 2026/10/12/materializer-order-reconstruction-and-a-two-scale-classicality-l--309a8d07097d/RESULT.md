# Materializer-order reconstruction and a two-scale classicality law in Boolean-topped Heyting chains

## Finding
For integers \(n,k\ge1\), let \(B_n=\mathcal P([n])\) and define the Heyting algebra \(H_{n,k}=B_n\oplus C_k\): its elements are the subsets of \([n]\), followed by \(k\) additional upper points \(t_1<\cdots<t_k\), each above every subset. The bottom is \(\varnothing\) and the top is \(t_k\). Implication is the relative pseudocomplement in this finite distributive lattice, and \(\neg x=x\to\varnothing\).

For \(x\in H_{n,k}\), define its **materializer**
\[
M(x)=\{y\in H_{n,k}:x\to y=\neg x\vee y\}.
\]
The complete family, with \(B_n\) identified with its subsets, is
\[
\begin{aligned}
M(\varnothing)&=M(t_k)=H_{n,k},\\
M(S)&=\{T\subseteq[n]:S\not\subseteq T\}\cup\{t_k\}\quad(\varnothing\ne S\subseteq[n]),\\
M(t_i)&=B_n\cup\{t_1,\dots,t_{i-1},t_k\}\quad(1\le i<k).
\end{aligned}
\]
In particular the inclusion-ordered set of distinct materializers is isomorphic to
\[
\big(B_n\setminus\{\varnothing\},\subseteq\big)\oplus C_k.
\]
For \(n\ge2\), this order determines \(n\) (the number of its minimal elements) and then \(k\) (the number of remaining elements beyond the \(2^n-1\) nonempty Boolean subsets). For \(n=1\) the order is a chain of length \(k+1\); this chain case is distinguished from \(n\ge2\) by having only one minimal element.

The exact number of ordered failures of material implication and the satisfiability degree are
\[
\begin{aligned}
F_{n,k}&=3^n-2^n+(2^n-1)(k-1)+\frac{k(k-1)}2,\\
\mathrm{ds}_{H_{n,k}}(x\to y=\neg x\vee y)&=1-\frac{F_{n,k}}{(2^n+k)^2}.
\end{aligned}
\]
For any integer sequence \(k_n\ge1\), if \(k_n/2^n\to c\) in the extended nonnegative reals, then
\[
\lim_{n\to\infty}\mathrm{ds}_{H_{n,k_n}}=\frac12+\frac{1}{2(1+c)^2},
\]
with the last summand interpreted as zero at \(c=\infty\). Consequently the two iterated limits with respect to \(n,k\) do not commute:
\[
\lim_{k\to\infty}\lim_{n\to\infty}\mathrm{ds}_{H_{n,k}}=1,
\qquad
\lim_{n\to\infty}\lim_{k\to\infty}\mathrm{ds}_{H_{n,k}}=\frac12.
\]

## Assumptions and scope
All algebras are finite, nontrivial, and use the full Heyting signature. The ordinal sum here **retains the Boolean top** \([n]\) as a distinct element immediately below \(t_1\). The chain \(C_k\) contributes \(k\) new points; hence \(|H_{n,k}|=2^n+k\). The two-variable equation is evaluated on uniformly random, independently chosen ordered elements; no assumption about distribution of formulas or proof systems is needed.

## Proof
Write \(b=2^n\). For every nonempty Boolean set \(S\), its negation is the Boolean complement \([n]\setminus S\). If \(T\in B_n\), then
\[
S\to T=\begin{cases}t_k,&S\subseteq T,\\([n]\setminus S)\cup T,&S\not\subseteq T.\end{cases}
\]
For \(S\ne\varnothing\), \(S\to t_j=t_k\) for all \(j\), while \(\neg S\vee t_j=t_j\). If \(x=t_i\), then \(\neg x=\varnothing\), \(t_i\to T=T\) for \(T\in B_n\), and
\[
t_i\to t_j=\begin{cases}t_k,&i\le j,\\t_j,&i>j.\end{cases}
\]
Finally, \(\neg\varnothing=t_k\); material implication holds for every consequent when the antecedent is \(\varnothing\). These identities follow immediately from \(a\to b=\max\{z:a\wedge z\le b\}\) and exhaust all antecedent/consequent types.

They yield the materializer formulas in the Finding. For nonempty Boolean \(S,T\), the equivalence
\[
M(S)\subseteq M(T)\iff S\subseteq T
\]
follows by complementing the corresponding Boolean principal filters. All Boolean materializers lie strictly below \(M(t_1)\), the \(k\) upper materializers form a strict chain, and no further distinct materializers occur. This proves the inclusion-order classification and parameter recovery.

The failures partition into three disjoint classes:
(1) Boolean \(S\ne\varnothing\) and Boolean \(T\supseteq S\), giving \(\sum_{S\ne\varnothing}2^{n-|S|}=3^n-2^n\);
(2) Boolean \(S\ne\varnothing\) and one of \(t_1,\ldots,t_{k-1}\), giving \((b-1)(k-1)\);
(3) \(t_i\to t_j\) with \(1\le i\le j<k\), giving \(k(k-1)/2\).
Their sum is \(F_{n,k}\). Dividing by \((b+k)^2\) proves the exact degree.

For the asymptotic law divide the numerator and denominator by \(b^2\). Since \((3/4)^n\to0\), the term \((3^n-2^n)/b^2\to0\). When \(k/b\to c<\infty\), the failure probability tends to \((c+c^2/2)/(1+c)^2\), whose complement equals \(1/2+1/(2(1+c)^2)\). If \(k/b\to\infty\), direct division by \(k^2\) shows the failure probability tends to \(1/2\). The iterated limits follow, including the fixed-\(n\) limit as \(k\to\infty\).

## Verification
The standalone `verify_materializers.py` constructs each finite lattice directly, computes its implication as the greatest element satisfying the adjunction, and checks the theorem's claimed sets, inclusions, distinct counts and failure count without using the closed formula to generate the implication values. It exhaustively checks \(1\le n\le5\), \(1\le k\le6\): 30 algebras and 11,243 ordered implication pairs. Invocation: `python3 verify_materializers.py`. Observed output: `VERIFY_OK cases 30 material_implication_pairs 11243 materializer_orders_checked 30`. The unrestricted theorem is proved above; these finite checks are not an exhaustive proof for larger parameters.

## Relationship to prior work
Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (arXiv:2110.11515; DOI:10.1017/jsl.2024.2), introduce materializers and identify qualitative properties in §3.13–3.14. Their §3.15 establishes the absence of a uniform finite satisfiability gap by a lower bound for the special case of adjoining **one** new top to a Boolean algebra. That qualitative result and its lower bound are prior work. The claim here gives an exact materializer inclusion structure, an exact ordered-failure census throughout the two-parameter Boolean-plus-chain family, and its two-scale asymptotic law. The present formulation does not assert a new no-gap theorem or a new general Heyting-algebra identity.

## Limitations
This calculation addresses only the specified ordinal-sum family; it does not classify materializers of arbitrary finite Heyting algebras. The phase law is an asymptotic statement for the stated scaling regimes, not a finite-size estimate uniform across all parameters. The inclusion poset for \(n=1\) is a chain; the explicit reconstruction argument for \(n\ge2\) must not be applied to its chain shape. Related unpublished or differently indexed exact enumerations remain possible; independent validation has not been performed.

## References
1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first posted 2021-10-21, §§1.10–1.16, 3.13–3.16; DOI:10.1017/jsl.2024.2. Lawfully accessible manuscript: https://arxiv.org/pdf/2110.11515.
2. The same work, *Journal of Symbolic Logic* 90 (2025), 533–551, DOI:10.1017/jsl.2024.2; publication date is not used as the earliest public source date.
