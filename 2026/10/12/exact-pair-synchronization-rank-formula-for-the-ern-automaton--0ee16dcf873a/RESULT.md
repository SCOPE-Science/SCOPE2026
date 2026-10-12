# Exact pair-synchronization rank formula for the Černý automaton
## Finding
Fix \(n\ge2\). On \(Q=\mathbb Z/n\mathbb Z\), consider the Černý automaton
\[
a(i)=i+1\pmod n,
\qquad
b(n-1)=0,\quad b(i)=i\ \text{for }i<n-1.
\]
For an unordered pair \(S\subset Q\), let \(t_n(S)\) be the minimum length of a word sending both states of \(S\) to one state.

For
\[
S=\{i,j\},\qquad 0\le i<j<n,
\]
put \(g=j-i\). Then
\[
t_n(\{i,j\})
=
\min\{\,gn-i,\ (n-g)n-j\,\}.
\]

Equivalently, let \(r\) be the smaller circular separation of the pair. Write
\[
S=P(r,x)=\{x,x+r\pmod n\}
\]
using the unique orientation with \(1\le r<n/2\); when \(n\) is even and \(r=n/2\), choose the unique representative with \(n/2\le x<n\). Then
\[
t_n(P(r,x))=(r-1)n+n-x.
\]

Thus the formula gives a state-by-state rank coordinate on the entire pair layer. In particular the unique pair of every weight
\[
1,2,\ldots,\binom n2
\]
is determined explicitly; the unique hardest pair in this labeling is
\[
\{0,\lfloor n/2\rfloor\},
\]
and for a uniformly chosen unordered pair,
\[
\mathbb E\,t_n(S)
=
\frac{\binom n2+1}{2}
=
\frac{n^2-n+2}{4}.
\]

## Assumptions and scope
Words act from left to right. The convention above is conjugate to the common presentation in which the cyclic letter acts on \(\{1,\ldots,n\}\) and the singular letter maps \(1\) to \(2\) while fixing the other states: the relabeling \(q\mapsto q+2\pmod n\) carries one presentation to the other.

The weight \(t_n(S)\) is the shortest-path distance from the pair \(S\) to the singleton layer of the power automaton. The theorem concerns only the two-state layer of the Černý automaton; it does not give analogous formulas for \(k\)-sets with \(k\ge3\).

The published rendezvous-time literature already proves that the maximum pair weight in the Černý automaton is \(\binom n2\). That extremal fact by itself forces the abstract multiset of pair weights to be \(1,\ldots,\binom n2\) along a geodesic through all pair states. The contribution proved here is the closed formula assigning the exact weight to each labeled pair, together with the resulting canonical rank coordinate.

## Proof
For a pair \(S\), define its canonical coordinates \(P(r,x)\) as in the finding and set
\[
D(P(r,x))=(r-1)n+n-x.
\]
We prove that \(D(S)\) is exactly the shortest synchronization distance.

First, every pair has a unique canonical coordinate. For \(r<n/2\), the shorter oriented arc determines \(x\) uniquely. If \(n\) is even and \(r=n/2\), the two orientations are tied, and the condition \(n/2\le x<n\) chooses one of them.

Consider the action of \(a\). If \(x<n-1\), then
\[
P(r,x)a=P(r,x+1)
\]
and therefore
\[
D(P(r,x)a)=D(P(r,x))-1.
\]
If \(x=n-1\), the cyclic wrap changes the canonical representative and cannot decrease \(D\) by more than one.

Now consider \(b\). If the pair does not contain \(n-1\), it is fixed. If \(x=n-1\), then
\[
P(r,n-1)=\{n-1,r-1\}.
\]
For \(r=1\), \(b\) synchronizes the pair. For \(r>1\),
\[
P(r,n-1)b=P(r-1,0),
\]
so in both cases the rank drops by exactly one:
\[
D(P(r,n-1)b)=D(P(r,n-1))-1.
\]

It remains to check the case in which \(n-1\) is the other endpoint. Then \(r<n/2\) and \(x=n-1-r\). If \(2r+2<n\), applying \(b\) changes the shorter circular separation from \(r\) to \(r+1\), and the new rank is \(D+n\). If \(2r+2=n\), the image is diametric and again its rank is \(D+n\). If \(2r+1=n\), the maximal odd separation is preserved and the new rank is at least \(D\). Hence \(b\) never lowers \(D\) by more than one. The same is already clear for \(a\) from the preceding cases. Therefore every single letter satisfies
\[
D(S\ell)\ge D(S)-1,
\qquad \ell\in\{a,b\},
\]
with singleton rank defined as \(0\).

This proves the lower bound
\[
t_n(S)\ge D(S),
\]
because no word can reduce the rank from \(D(S)\) to \(0\) faster than one unit per letter.

For the reverse inequality, start from \(P(r,x)\). Apply
\[
a^{\,n-1-x}b.
\]
This takes the canonical start to \(n-1\) and then reduces \(r\) by one; when \(r=1\), it synchronizes. After the first reduction, the new pair is \(P(r-1,0)\), so each further reduction uses
\[
a^{\,n-1}b
\]
and costs exactly \(n\) letters. The total length is
\[
(n-x)+(r-1)n=D(P(r,x)).
\]
Thus
\[
t_n(P(r,x))=D(P(r,x)).
\]

To convert to ordinary coordinates, let \(S=\{i,j\}\) with \(i<j\) and \(g=j-i\). If the forward gap \(g\) is the chosen shorter arc, then \(r=g\) and \(x=i\), giving \(gn-i\). If the backward gap \(n-g\) is chosen, then \(r=n-g\) and \(x=j\), giving \((n-g)n-j\). In the diametric case the canonical convention chooses the second expression. Hence
\[
t_n(\{i,j\})
=
\min\{gn-i,(n-g)n-j\}.
\]

Finally, for fixed non-diametric \(r\), the values
\[
(r-1)n+n-x,\qquad 0\le x<n,
\]
are precisely the consecutive block
\[
(r-1)n+1,\ldots,rn.
\]
When \(n\) is even, the final diametric layer \(r=n/2\) contributes the remaining \(n/2\) values up to \(\binom n2\). This also gives the stated unique hardest pair and mean.

## Verification
Run `python3 verify.py` beside `certificate.json`.

For every \(2\le n\le80\), the verifier builds the complete singleton-and-pair subgraph of the power automaton and computes exact shortest distances to the singleton layer by reverse breadth-first search. It compares every pair distance with the closed formula.

Independently, it checks the rank potential under both letters: neither letter can reduce the proposed rank by more than one, while at least one letter always realizes a one-unit decrease. It also verifies that the weights form exactly the interval
\[
1,\ldots,\binom n2,
\]
that the hardest pair is unique, and that the exact sum agrees with the stated mean.

These finite computations are regression checks. The theorem for every \(n\) follows from the rank argument above, not from extrapolation.

## Relationship to prior work
Behague and Johnson define the weight \(t(S)\) of a synchronizable set as its shortest path to a singleton and study the extremal quantities \(\operatorname{rdv}(k,n)\) and \(\operatorname{RDV}(k,n)\). For pairs they prove
\[
\operatorname{RDV}(2,n)=\binom n2
\]
and use the pair
\[
\{2,\lfloor n/2\rfloor+2\}
\]
in the Černý automaton as an extremal example. Under the relabeling used here, that pair is exactly \(\{0,\lfloor n/2\rfloor\}\).

That published maximum already implies, by following a shortest geodesic of length \(\binom n2\), that the pair layer contains weights \(1,\ldots,\binom n2\). This consequence is therefore not claimed as the originality of the present result. What is added here is the explicit target-by-target formula
\[
t_n(\{i,j\})=\min\{(j-i)n-i,\ (n-j+i)n-j\},
\]
or equivalently the canonical rank \(D(P(r,x))=(r-1)n+n-x\). It identifies which labeled pair has each weight and supplies a simple monotone rank certificate for every shortest pair-synchronizing path.

The same paper cites Cardoso's thesis for stronger lower bounds on \(k\)-set weights in the Černý automaton. Repository metadata for that thesis was located, but its body was not available through the bounded public-access route used here. The later paper summarizes Cardoso's relevant result as a \(k\)-set extremal lower bound, not as a pair-by-pair distance formula; the unavailable thesis remains a residual literature risk.

## Limitations
The formula is specific to the classical Černý automaton and the pair layer. It does not determine exact weights of arbitrary \(k\)-sets with \(k\ge3\), where the geometry is substantially more complicated.

The abstract fact that all pair weights \(1,\ldots,\binom n2\) occur is already an immediate implication of the published extremal pair result; only the labeled closed formula and rank structure are asserted here as new.

A 2014 thesis on synchronization is a plausible older source whose full text was not recovered through the bounded access path used for this review. No exact formula equivalent to the one above was found in the inspected literature or targeted searches, but this access limitation is retained as an originality risk.

## References
1. N. C. Behague and J. R. Johnson, “Synchronizing Times for \(k\)-sets in Automata,” arXiv:2008.12166v1, first public 2020-08-27; *The Electronic Journal of Combinatorics* 29(3) (2022), #P3.41, DOI 10.37236/9819.
2. F. Gonze and R. M. Jungers, “On the Synchronizing Probability Function and the Triple Rendezvous Time for Synchronizing Automata,” *SIAM Journal on Discrete Mathematics* 30 (2016), 995–1014, DOI 10.1137/15M1024603.
3. Â. F. P. Cardoso, *The Černý Conjecture and Other Synchronization Problems*, Ph.D. thesis, University of Porto, 2014, DOI 10.34626/607f-t921.
