# Exact onset for two-degree-window spread at minimum degree one

## Result

For a graph \(G\), let
\[
\operatorname{sp}(G,1)=\max_j\bigl|\{v\in V(G):\deg(v)\in\{j,j+1\}\}\bigr|.
\]
Fix an integer average degree \(d\ge 2\). An order \(n\) is called admissible when \(nd\) is even, so that a graph of order \(n\) and average degree \(d\) can have an integral number of edges.

**Theorem.** For every admissible \(n\ge 2d+1\), there is a simple graph \(G\) of order \(n\), minimum degree \(1\), and average degree \(d\) such that
\[
\boxed{\operatorname{sp}(G,1)=\left\lceil\frac nd\right\rceil.}
\]
At \(n=2d\), the maximised Caro--Škrekovski--Zarb bound equals \(2\), but every graph of order at least three has \(\operatorname{sp}(G,1)\ge 3\). Moreover, graphs with order \(2d\), minimum degree \(1\), and average degree \(d\) do exist. Consequently, in the admissible-order sense of Problem 22 of Caro--Škrekovski--Zarb,
\[
\boxed{n_0(1,1,d)=2d+1\qquad(d\in\mathbb Z,\ d\ge2).}
\]

Thus this specialization attains exactly the linear onset suggested in Problem 22, improving the general quadratic sufficient threshold for these parameters.

## Why the target value is \(\lceil n/d\rceil\)

Caro--Škrekovski--Zarb write \(h=k+1\) and \(x=(d-\delta)/h\). For \((\delta,k)=(1,1)\),
\[
h=2,\qquad x=\frac{d-1}{2},\qquad 2x=d-1\in\mathbb Z.
\]
Their Proposition 4 therefore gives
\[
\max_{t\ge1}f_t=\frac{n}{2x+1}=\frac nd,
\]
and their Theorem 8 identifies the maximised integer-sequence bound as
\[
s^*=\max_t\lceil f_t\rceil=\left\lceil\frac nd\right\rceil.
\]
Hence only graphicality of a degree sequence with this window number remains.

## The obstruction at \(n=2d\)

At \(n=2d\), the maximised bound is \(2\). The Erdős--Chen--Rousseau--Schelp theorem gives \(\operatorname{sp}(G,1)\ge3\) for every graph of order at least three, so equality with the maximised bound is impossible.

The parameter class is nonempty at this order. Choose any connected graph \(H\) on \(2d-1\) vertices with \(d^2-1\) edges; this is possible because
\[
2d-2\le d^2-1\le \binom{2d-1}{2}.
\]
Attach one new leaf to a vertex of \(H\). The resulting graph has \(2d\) vertices, \(d^2\) edges, minimum degree \(1\), and average degree \(d\).

It remains to construct an extremal graphical sequence for every admissible \(n\ge2d+1\).

## Range I: \(2d+1\le n<3d\)

Put
\[
a=n-(2d-1),\qquad 2\le a\le d,
\]
and define the multiset
\[
D_{d,a}=\{1,2,\ldots,2d-1\}\uplus
\{d-a+1,d-a+3,\ldots,d+a-1\}.
\]
It has length \(n\), minimum \(1\), and
\[
\sum D_{d,a}=d(2d-1)+ad=dn.
\]
The second displayed set has step two, so every pair of consecutive integers contains at most one of its terms. Since the base set contains each degree once, every two-degree window contains at most three entries, and at least one contains three. Hence
\[
\operatorname{sp}(D_{d,a},1)=3=\left\lceil\frac nd\right\rceil.
\]

It remains to prove that \(D_{d,a}\) is graphic whenever its sum is even. We verify Erdős--Gallai directly. Let \(M=2d-1\), let
\[
B=(M,M-1,\ldots,1),
\]
and write \(F_X(k)\) for the Erdős--Gallai right side minus left side at index \(k\) for a nonincreasing list \(X\). Straight summation gives
\[
F_B(k)=
\begin{cases}
-k,&1\le k\le d,\\
2z^2-d,&k=d+z,\ 0\le z\le d-1.
\end{cases}
\]
Write \(\ell=d-a+1\). Among the top \(k\) terms of \(D_{d,a}\), suppose \(r\) terms come from the added step-two set. They displace the \(r\) smallest terms of the top \(k\) terms of \(B\), namely
\[
t_j=M-k+j\qquad(1\le j\le r),
\]
while the \(r\) added terms in the top block are the \(r\) largest added terms and have total
\[
r(d+a-r).
\]
All added terms outside the top block are at least \(\ell\).

For \(k\le d\), every added term improves the slack by at least \(\min\{k,\ell\}\). Therefore
\[
F_{D_{d,a}}(k)\ge-k+a\min\{k,\ell\}\ge0.
\]
Indeed, if \(k\le\ell\) this is immediate, while if \(k>\ell\),
\[
a\ell=a(d-a+1)\ge d\ge k,
\]
because \(a(d-a+1)-d=(a-1)(d-a)\ge0\).

Now let \(k=d+z\) with \(z\ge1\). If \(r\le2z\), summing the displaced terms gives
\[
F_{D_{d,a}}(k)\ge
(a-1)(d-a)+2\bigl(r^2-(z+1)r+z^2\bigr)\ge0.
\]
The quadratic is nonnegative: for \(z=1\) it is \((r-1)^2\), and for \(z\ge2\) its discriminant \(-3z^2+2z+1\) is negative.

If \(r>2z\), then the terms \(t_j\) with \(j>2z\) have crossed the truncation point in the Erdős--Gallai right side. Accounting for that truncation yields
\[
F_{D_{d,a}}(k)\ge
(a-1)(d-a)+\frac32r(r-1)-z>0,
\]
since \(r\ge2z+1\). Finally, for \(k\ge2d\), the maximum term is \(2d-1\le k-1\), so the Erdős--Gallai inequality is automatic. Thus \(D_{d,a}\) is graphic.

## The endpoint \(n=3d\)

This order is admissible only when \(d\) is even. Use
\[
P_d=\{1^3,3^3,5^3,\ldots,(2d-1)^3\},
\]
where exponents denote multiplicities. It has length \(3d\), sum \(3d^2\), minimum degree \(1\), and every two-degree window contains exactly one odd degree value, with multiplicity three. Hence \(\operatorname{sp}(P_d,1)=3\).

For graphicality, the Tripathi--Vijay reduction of Erdős--Gallai lets us check only the ends of equal-degree blocks, \(k=3r\). Dividing the Erdős--Gallai slack by three gives
\[
Q(r)-C(B_r),
\]
where
\[
Q(r)=5r^2-(4d+1)r+d^2,
\qquad
B_r=2d-5r-1,
\]
and \(C(B)=B+(B-2)+(B-4)+\cdots\) over positive terms. If \(B_r\le0\), then \(C(B_r)=0\) and \(Q(r)\ge0\): for \(d\ge3\) the discriminant of \(Q\) is \(-4d^2+8d+1<0\), while the only exceptional small case \(d=2\) is immediate. If \(B_r>0\), then
\[
C(B_r)\le\frac{(B_r+1)^2}{4}=\frac{(2d-5r)^2}{4},
\]
so
\[
Q(r)-C(B_r)\ge\frac{r(4d-5r-4)}4>0,
\]
because \(B_r>0\) implies \(5r<2d-1\). Thus \(P_d\) is graphic.

## Range II: \(3d<n<4d-2\)

Put
\[
a=n-(2d-1),\qquad d+2\le a\le2d-2.
\]
Choose a symmetric set \(E_{d,a}\subseteq\{1,\ldots,2d-1\}\) of size \(a\) and mean \(d\): if \(a=2q\), take
\[
E_{d,a}=\{d-j,d+j:1\le j\le q\},
\]
and if \(a=2q+1\), take
\[
E_{d,a}=\{d-q,d-q+1,\ldots,d+q\}.
\]
Now let
\[
R_{d,a}=\{1,2,\ldots,2d-1\}\uplus E_{d,a}.
\]
Then \(|R_{d,a}|=n\), \(\sum R_{d,a}=dn\), and every degree from \(1\) through \(2d-1\) occurs, so the list is gap-free. Every multiplicity is at most two; hence each two-degree window has size at most four. Since \(a\ge d+2\), the set \(E_{d,a}\) contains two consecutive degrees, so some window has size four. Therefore
\[
\operatorname{sp}(R_{d,a},1)=4=\left\lceil\frac nd\right\rceil.
\]

Barrus--Hartke--Jao--West proved that a positive gap-free even-sum list with largest term \(r\) and smallest term \(s\) is graphic whenever its length is at least
\[
r+\frac{r+s+1}{2s}.
\]
Here \(r=2d-1\), \(s=1\), so the threshold is \(3d-\tfrac12\). Since \(n>3d\), every admissible \(R_{d,a}\) is graphic.

## Range III: \(n\ge4d-2\)

Let
\[
s=\left\lceil\frac nd\right\rceil,
\qquad
b=n-(s-1)d\in\{1,\ldots,d\}.
\]
Define \(L_{d,n}\) by taking \(s-1\) copies of every odd degree
\[
1,3,5,\ldots,2d-1
\]
and one extra copy of every term in
\[
d-b+1,d-b+3,\ldots,d+b-1.
\]
The latter progression has \(b\) terms and mean \(d\). Thus
\[
|L_{d,n}|=(s-1)d+b=n,
\qquad
\sum L_{d,n}=(s-1)d^2+bd=dn.
\]
The extra progression has one parity and step two. Therefore a two-degree window either contains an odd baseline degree with multiplicity \(s-1\), or that baseline together with one extra term, or an odd degree whose own multiplicity has been raised to \(s\). Hence
\[
\operatorname{sp}(L_{d,n},1)=s=\left\lceil\frac nd\right\rceil.
\]

To prove graphicality, apply Cloteaux's sum-sensitive sufficient condition. For a list of length \(n\), maximum \(A\), minimum \(a_0\), and even sum \(S\), it suffices that
\[
(A-a_0)\left(\frac{n-A-1}{nA-S}+\frac{a_0}{S-na_0}\right)\ge1.
\]
For \(L_{d,n}\),
\[
A=2d-1,\qquad a_0=1,\qquad S=nd,
\]
and the left side simplifies exactly to
\[
\frac{2(n-2d+1)}{n}.
\]
This is at least one precisely when \(n\ge4d-2\). Hence every admissible \(L_{d,n}\) in this range is graphic.

The three ranges and the endpoint cover every admissible \(n\ge2d+1\), completing the proof.

## Verification

The proof is general and does not rely on computation. The accompanying standalone script `artifacts/verify_degree_spread.py` independently constructs the displayed sequences and checks their lengths, sums, minimum and maximum degrees, two-degree window numbers, and the full Erdős--Gallai criterion for every admissible pair
\[
2\le d\le100,\qquad 2d+1\le n\le8d.
\]
It checks 22,797 parameter pairs. It was executed successfully with Python 3.13.5.

## Literature context and originality

Caro--Škrekovski--Zarb introduced the explicit eventual-exactness threshold problem in their 17 September 2026 preprint and asked in Problem 22 for the smallest \(n_0(\delta,k,d)\), noting computational evidence for a linear \(2d+O(k+1)\) onset rather than their quadratic general threshold. Their Proposition 4 and Theorem 8 reduce the present specialization to graphical realization of an optimal window count, but no exact value of \(n_0(1,1,d)\) is stated there.

Caro--Lauri--Zarb's earlier work supplies the universal \(\operatorname{sp}(G,k)\ge k+2\) obstruction used at \(n=2d\). Barrus--Hartke--Jao--West and Cloteaux provide graphicality criteria used in the proof, but do not formulate the degree-spread onset problem.

Searches for the exact specialization, the equivalent two-consecutive-degree window formulation, the formula \(n_0(1,1,d)=2d+1\), and combinations of minimum degree one with \(\operatorname{sp}(G,1)\) found no prior statement of this result. Originality is therefore claimed only **to the best of our knowledge**. The principal residual risk is unindexed parallel work because the motivating preprint is extremely recent.

## Limitations

- The theorem treats only \(\delta=1\), \(k=1\), and integer average degree \(d\ge2\).
- The threshold is interpreted over admissible orders \(n\) with \(nd\) even; no graph of average degree \(d\) exists when \(nd\) is odd.
- No formula is claimed here for nonintegral fixed average degree, other minimum degrees, or wider windows.


## References

1. Y. Caro, R. Škrekovski, C. Zarb, *Spreads of degrees in graphs*, arXiv:2609.19762 (2026). https://arxiv.org/abs/2609.19762
2. Y. Caro, J. Lauri, C. Zarb, *Notes on Spreads of Degrees in Graphs*, Bull. Inst. Combin. Appl. 85 (2019), 79--91; arXiv:1806.08303. https://arxiv.org/abs/1806.08303
3. M. D. Barrus, S. G. Hartke, K. F. Jao, D. B. West, *Length thresholds for graphic lists given fixed largest and smallest entries and bounded gaps*, Discrete Math. 312 (2012), 1494--1501. https://doi.org/10.1016/j.disc.2011.05.001
4. B. Cloteaux, *A Sufficient Condition for Graphic Sequences with Given Largest and Smallest Entries, Length, and Sum*, Discrete Math. Theor. Comput. Sci. 20 (2018), #25. https://doi.org/10.23638/DMTCS-20-1-25
5. A. Tripathi, S. Vijay, *A note on a theorem of Erdős & Gallai*, Discrete Math. 265 (2003), 417--420. https://doi.org/10.1016/S0012-365X(02)00886-5
