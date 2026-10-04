# Bridge factorization of power domination polynomials for proper double stars
## Finding
Let \(D_{a,b}\), with \(a,b\ge2\), be the tree formed from adjacent centers \(u,v\), with \(a\) leaves adjacent to \(u\) and \(b\) leaves adjacent to \(v\). A set \(S\subseteq V(D_{a,b})\) is power dominating if and only if
\[
u\in S\ \text{ or }\ |S\cap L_u|\ge a-1,\qquad v\in S\ \text{ or }\ |S\cap L_v|\ge b-1.
\]
Consequently, if \(Q_t(x)=x(1+x)^t+t x^{t-1}+x^t=\mathcal P(K_{1,t};x)\), then the connected bridge composition factors exactly as
\[
\mathcal P(D_{a,b};x)=Q_a(x)Q_b(x).
\]
Hence \(\mathcal P(D_{a,b};1)=(2^a+a+1)(2^b+b+1)\), \(\gamma_P(D_{a,b})=2\), and the number of minimum power dominating sets is \(c(a)c(b)\), where \(c(2)=3\) and \(c(t)=1\) for \(t\ge3\). In particular, when \(a,b\ge3\), the unique minimum power dominating set is \(\{u,v\}\).

## Assumptions and scope
All graphs are finite and simple. For integers \(a,b\ge2\), the proper double star \(D_{a,b}\) has adjacent centers \(u,v\), a leaf set \(L_u\) of size \(a\) adjacent only to \(u\), and a leaf set \(L_v\) of size \(b\) adjacent only to \(v\).

A set \(S\) is power dominating when the following observation process reaches every vertex: first observe \(N[S]\); thereafter, whenever an observed vertex has exactly one unobserved neighbor, observe that neighbor. Write \(\mathcal P(G;x)=\sum_S x^{|S|}\), where the sum ranges over all power dominating sets of \(G\).

## Proof
Suppose first that \(u\notin S\) and that at least two vertices of \(L_u\) are outside \(S\). Those omitted leaves can only be observed by \(u\). The center \(u\) may eventually become observed through \(v\) or through a selected leaf in \(L_u\), but while at least two of its leaf neighbors remain unobserved, \(u\) cannot force either one. No other vertex is adjacent to those leaves. Thus \(S\) is not power dominating. Therefore every power dominating set satisfies
\[
u\in S\quad\text{or}\quad |S\cap L_u|\ge a-1.
\]
The same argument at \(v\) gives
\[
v\in S\quad\text{or}\quad |S\cap L_v|\ge b-1.
\]

Conversely, assume both displayed side conditions. If a center belongs to \(S\), its whole leaf side is observed in the domination step. If a center does not belong to \(S\), at least all but one of its leaves are selected; those selected leaves observe the center in the domination step, and after the opposite center is observed there is at most one unobserved leaf on that side, which its center forces. Hence both side conditions are sufficient.

The characterization separates the choice on \(\{u\}\cup L_u\) from the choice on \(\{v\}\cup L_v\). On a side with \(t\) leaves, either the center is selected and the leaves are arbitrary, contributing
\[
x(1+x)^t,
\]
or the center is not selected and one chooses either \(t-1\) or \(t\) leaves, contributing
\[
tx^{t-1}+x^t.
\]
Thus the side polynomial is
\[
Q_t(x)=x(1+x)^t+t x^{t-1}+x^t,
\]
and multiplication of the two independent side choices yields
\[
\mathcal P(D_{a,b};x)=Q_a(x)Q_b(x).
\]
The same \(Q_t\) is the published power domination polynomial of the star \(K_{1,t}\), so this is an exact bridge factorization into the two star factors.

Evaluating at \(x=1\) gives \(Q_t(1)=2^t+t+1\), proving the total count. The least exponent of \(Q_t\) is one. Its coefficient is three for \(t=2\) and one for \(t\ge3\), so the product has minimum exponent two and the stated minimum-set count.

## Verification
The included checker independently constructs every \(D_{a,b}\) with \(2\le a,b\le7\). For every vertex subset it simulates the domination step and subsequent forcing rule directly, without using the structural theorem to decide success. It separately tests the side-condition characterization, expands \(Q_a(x)Q_b(x)\) by integer polynomial multiplication, and compares every coefficient, the total count, the minimum exponent, and the minimum-set multiplicity.

## Relationship to prior work
The foundational power-domination-polynomial paper defines the invariant, derives decomposition formulas, and computes several standard graph families. In particular, its star formula specializes to
\[
\mathcal P(K_{1,t};x)=x(1+x)^t+t x^{t-1}+x^t=Q_t(x).
\]
Its conclusion explicitly identifies counting power dominating sets of nontrivial tree families and splitting formulas based on cut vertices or separating sets as directions for further work.

The present theorem is not the ordinary disjoint-union multiplicativity from that paper: \(D_{a,b}\) is connected, and the two star centers are joined by a bridge. Nor is it a consequence of the previously derived spider-tree polynomial: a spider has one branching center, whereas a proper double star has two adjacent branching centers. A later same-invariant article derives power domination polynomials for several other named families; targeted full-text searches of that article and targeted literature searches found no double-star or bistar power-domination polynomial.

## Limitations
The theorem is restricted to proper double stars with \(a,b\ge2\); degenerate one-sided cases have different minimum-coefficient behavior and are not claimed. The computational verification is finite corroboration only; the arbitrary-parameter statement follows from the proof. Search coverage cannot rule out an unindexed or differently phrased bistar enumeration.

## References
1. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, “Power domination polynomials of graphs,” arXiv:1805.10984v1, 28 May 2018, MSC 05C31, 05C15.
2. K. Geethu, A. Parthiban, “On Graph Entropy Measures Based on the Number of Dominating and Power Dominating Sets,” Malaysian Journal of Mathematical Sciences 19(1) (2025), 269–287, DOI 10.47836/mjms.19.1.14.
