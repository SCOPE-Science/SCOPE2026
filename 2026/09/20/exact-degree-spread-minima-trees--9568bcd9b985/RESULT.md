# Exact fixed-order degree-spread minima for trees

For a graph \(G\) and integer \(k\ge 0\), let
\[
\operatorname{sp}(G,k)
=
\max_{a\ge 0}
\left|\{v\in V(G): a\le d_G(v)\le a+k\}\right|.
\]
Thus \(\operatorname{sp}(G,0)=\operatorname{rep}(G)\), the maximum multiplicity of a vertex degree.

For \(n\ge2\), define
\[
\tau_k(n)=\min\{\operatorname{sp}(T,k):T\text{ is a tree on }n\text{ vertices}\}.
\]

## Theorem

For every \(n\ge2\),
\[
\boxed{\tau_0(n)=\left\lceil\frac{n+2}{3}\right\rceil.}
\]
For every \(k\ge1\),
\[
\boxed{
\tau_k(n)
=
n-\left\lfloor\frac{n-2}{k+1}\right\rfloor
=
\left\lceil\frac{kn+2}{k+1}\right\rceil.
}
\]

Hence the known lower bounds for tree degree spreads are sharp at every order, not only on congruence classes admitting the previously displayed two-degree constructions.

## Proof for \(k\ge1\)

Let
\[
H=\{v\in V(T):d_T(v)\ge k+2\}.
\]
For every tree,
\[
\sum_{v\in V(T)}(d_T(v)-1)=n-2.
\]
Every vertex in \(H\) contributes at least \(k+1\) to the left side, so
\[
|H|\le \left\lfloor\frac{n-2}{k+1}\right\rfloor=:q.
\]
All \(n-|H|\) remaining vertices have degree in the single interval
\(\{1,\ldots,k+1\}\), and therefore
\[
\operatorname{sp}(T,k)\ge n-q.
\]

It remains to realize equality for every \(n\). Write
\[
n-2=q(k+1)+r,\qquad 0\le r\le k.
\]
Consider the degree multiset
\[
\underbrace{k+2,\ldots,k+2}_{q\text{ times}},
\quad
\begin{cases}
r+1,&r>0,\\
\text{nothing},&r=0,
\end{cases}
\quad
\underbrace{1,\ldots,1}_{\text{all remaining vertices}}.
\]
The sum of \(d_i-1\) is \(q(k+1)+r=n-2\), so the degree sum is \(2n-2\). Every positive integer degree sequence with this sum is a tree degree sequence, for example by the Prüfer-code characterization.

The window \([1,k+1]\) contains exactly \(n-q\) vertices. If \(r=0\), the only other occupied degree is \(k+2\), with multiplicity \(q\). If \(r>0\), every competing width-\(k\) window contains at most the \(q\) vertices of degree \(k+2\) together with the one vertex of degree \(r+1\), hence at most \(q+1\) vertices. Since \(k\ge1\),
\[
q\le\left\lfloor\frac{n-2}{2}\right\rfloor,
\]
so \(q+1\le n-q\). Thus the displayed sequence has spread exactly \(n-q\).

Finally,
\[
n-\left\lfloor\frac{n-2}{k+1}\right\rfloor
=
\left\lceil\frac{kn+2}{k+1}\right\rceil.
\]

## Proof for \(k=0\)

Let \(n_i\) be the number of vertices of degree \(i\), and let
\[
R=\operatorname{rep}(T)=\max_i n_i.
\]
The standard leaf identity is
\[
n_1
=
2+\sum_{i\ge3}(i-2)n_i.
\]
Consequently
\[
\sum_{i\ge3}n_i
\le
\sum_{i\ge3}(i-2)n_i
=
n_1-2
\le R-2.
\]
Since \(n_1,n_2\le R\),
\[
n=n_1+n_2+\sum_{i\ge3}n_i\le 3R-2,
\]
and therefore
\[
R\ge\left\lceil\frac{n+2}{3}\right\rceil.
\]

This is attained at every order using only degrees \(1,2,3\). Write \(n=3q+s\), \(s\in\{0,1,2\}\). Use the following degree-count triples \((n_1,n_2,n_3)\):
\[
\begin{array}{c|c}
s&(n_1,n_2,n_3)\\ \hline
0&(q+1,q,q-1)\\
1&(q+1,q+1,q-1)\\
2&(q+2,q,q).
\end{array}
\]
The zero entries at the small boundary cases are allowed. In each row \(n_1=n_3+2\), so the degree sum is \(2n-2\); hence the multiset is realized by a tree. Its largest multiplicity is exactly \(\lceil(n+2)/3\rceil\).

## Relation to prior work

Caro and West introduced the repetition number and proved the general bound
\[
\operatorname{rep}(G)\ge
\left\lceil\frac{n}{2d-2\delta+1}\right\rceil.
\]
For trees this already implies the lower bound in the \(k=0\) theorem above; their tree construction establishes asymptotic sharpness rather than the exact fixed-order minimum for every \(n\).

Caro, Lauri and Zarb introduced the degree-spread parameter \(\operatorname{sp}(G,k)\). Their tree theorem gives, for \(k\ge1\),
\[
\operatorname{sp}(T,k)\ge\frac{nk+2}{k+1},
\]
and exhibits sharpness via trees whose degrees are only \(1\) and \(k+2\). That displayed construction requires the relevant degree multiplicities to be integral, equivalently \(n\equiv2\pmod{k+1}\). For \(k=0\) they state the lower bound \(\lceil n/3\rceil\) and sharpness on a congruence class.

The theorem here does not claim those lower bounds as new. Its contribution is the exact fixed-order extremal function for every \(n\), including all residue classes, with a one-intermediate-degree realization for \(k\ge1\) and explicit three-degree realizations for \(k=0\).

The recent paper of Caro, Škrekovski and Zarb revisits degree spreads and sharpness questions for general and maximal outerplanar graphs. Its accessible full text does not state this all-order tree formula.

## Verification

A standalone verifier enumerates every tree degree multiset through order \(40\). It uses the fact that a tree degree multiset is equivalent to a partition of \(n-2\) into the positive excesses \(d_i-1\), padded by zeros. For each multiset it evaluates the spread directly from the degree counts, and compares the exact minimum with the formulas above for \(0\le k\le\min(12,n+3)\). It separately checks the displayed witness degree sequences. The recorded run passed.

## Limitations and originality

The result concerns the extremal value over trees; it does not classify all extremal trees or all extremal degree sequences.

Originality is asserted only to the best of our knowledge. The primary sources inspected were Caro--West (2009), Caro--Lauri--Zarb (2019), and Caro--Škrekovski--Zarb (2026), together with searches under repetition number, degree multiplicity, degree spread, tree degree sequence, and equivalent fixed-order formulations. No source located states the two all-order formulas above as exact minima. No specific inaccessible source was identified as especially likely to contain the result. Differently phrased older degree-sequence literature and very recent unindexed work remain residual risks.

## References

1. Y. Caro and D. B. West, *Repetition Number of Graphs*, Electronic Journal of Combinatorics 16 (2009), R7. DOI: 10.37236/96.
2. Y. Caro, J. Lauri and C. Zarb, *Notes on Spreads of Degrees in Graphs*, Bulletin of the Institute of Combinatorics and its Applications 85 (2019), 79--91; arXiv:1806.08303.
3. Y. Caro, R. Škrekovski and C. Zarb, *Spreads of degrees in graphs*, arXiv:2609.19762 (submitted 17 September 2026).
