# Exact equilibrium-set dimension law for cycle public-goods games

## Finding

Consider the homogeneous local public-goods game on the cycle \(C_n\), for \(n\ge3\). Each player chooses \(x_i\ge0\) and receives payoff \(U_i=b(x_{i-1}+x_i+x_{i+1})-cx_i\), where indices are cyclic, \(b\in C^2([0,\infty))\), \(b'>0\), \(b''<0\), and the unique \(q>0\) satisfying \(b'(q)=c\) exists.

The full pure-Nash-equilibrium set has an exact block description. If every effort is positive, the equilibrium profile has period dividing three: it is uniform, \(x_i=q/3\), when \(3\nmid n\); when \(3\mid n\), it is a repetition of any positive triple \((a,b,d)\) with \(a+b+d=q\). If at least one effort is zero, every equilibrium is a cyclic concatenation of active singleton blocks \(S=(q)\) and active double blocks \(D(a)=(a,q-a)\), with \(0<a<q\), separated by zero gaps of length one or two. A length-two zero gap can occur only between singleton blocks. A length-one zero gap between consecutive double blocks \(D(a),D(b)\) requires \(b\ge a\); all other such gap conditions are automatic.

Consequently, the maximal semialgebraic dimension of the equilibrium set is

\[
d_{\max}(n)=\begin{cases}
\max\{2,n/3-2\},&n\equiv0\pmod3,\\
(n-4)/3,&n\equiv1\pmod3,\\
(n-2)/3,&n\equiv2\pmod3.
\end{cases}
\]

## Assumptions and scope

The cycle is simple and undirected. The payoff is a common strictly concave benefit of own effort plus the two neighbor efforts, minus a linear effort cost. Efforts are nonnegative and unbounded above. The statement concerns pure Nash equilibria only; it does not claim that every equilibrium is dynamically stable, welfare-maximizing, or robust under heterogeneous costs or edge weights.

## Proof

For fixed neighbor effort \(s=x_{i-1}+x_{i+1}\), strict concavity makes the unique best reply \(x_i=\max\{0,q-s\}\). Thus an equilibrium satisfies

\[
x_i>0\implies x_{i-1}+x_i+x_{i+1}=q,\qquad
x_i=0\implies x_{i-1}+x_{i+1}\ge q.
\]

If all coordinates are positive, subtraction of consecutive equalities gives \(x_{i+3}=x_i\). Cyclicity then forces the profile to be constant unless \(3\mid n\); in the latter case any positive triple summing to \(q\) repeats around the cycle. The all-positive branch therefore has dimension zero for \(3\nmid n\) and dimension two for \(3\mid n\).

Now suppose some coordinate is zero. A positive run of length at least three is impossible: at the first two positive vertices following a zero, the equilibrium equalities force the third effort in that run to be zero. A zero run of length at least three is impossible because its middle zero would have two zero neighbors, violating the zero-coordinate inequality. If a zero run has length two, each boundary zero forces the adjacent positive endpoint to be at least \(q\); that endpoint's own equality forces it to be at most \(q\), so it equals \(q\), and its other neighbor is zero. Hence both neighboring active blocks are singleton blocks \(S=(q)\).

A positive run of length one has effort \(q\). A positive run of length two must have efforts \(a,q-a\) with \(0<a<q\). Across a single zero between two such double blocks, the zero-coordinate inequality is \(q-a+b\ge q\), equivalent to \(b\ge a\). If either adjacent active block is a singleton, the inequality holds automatically. These conditions are both necessary and sufficient, proving the block description.

For a zero-containing block pattern, let \(s\) be the number of singleton active blocks, \(t\) the number of double active blocks, and \(r\) the number of length-two zero gaps. Then \(n=2s+3t+r\), with \(0\le r\le s\). If \(s\ge1\) and \(t>0\), in fact \(r\le s-1\), because each length-two zero gap needs an \(S\)-to-\(S\) adjacency in the cyclic word of active blocks and a double block prevents all singleton gaps from being such adjacencies. The double-block parameters form ordered chains with nonempty regions of dimension \(t\). If \(n=3k\), the candidate \(t=k-1\) leaves residual \(3\), impossible for \(s\ge1,t>0\) under this sharper bound; for \(k\ge3\), \(t=k-2\) leaves residual six and is realized by \(s=3,r=0\). If \(n=3k+1\), \(t=k-1\) leaves residual four, realized by \(s=2,r=0\); if \(n=3k+2\), \(t=k\) leaves residual two, realized by \(s=1,r=0\). If \(s=0\), all blocks are double blocks, \(n=3t\), and cyclic monotonicity forces all parameters equal, giving dimension one. Combining these dimensions with the all-positive branch gives the stated formula.

## Verification

The argument is an exact derivation from the best-response conditions; no finite enumeration is used as proof. The block constraints are sufficient as well as necessary, so the dimension count covers all pure equilibria under the stated assumptions. The formula does not extend automatically to directed cycles, nonuniform edge weights, heterogeneous benefit functions, or bounded effort sets.

## Relationship to prior work

Bramoullé and Kranton introduced the local public-goods model and gave general equilibrium conditions, a characterization of specialized equilibria by maximal independent sets, and examples of hybrid equilibria. Naghizadeh and Liu recast a broader network model as a linear complementarity problem and gave a matrix condition for uniqueness. The result here is a cycle-specific classification of all equilibrium strata and an explicit formula for the maximal semialgebraic dimension; it is not a new existence or stability theorem.

## Limitations

The classification relies on the unweighted cycle and a common interior target effort \(q\). The dimension is a measure of equilibrium-set degeneracy, not a prediction of which equilibrium is selected. No claim is made about generic perturbations of the network or about mixed-strategy equilibria outside the stated strictly concave model.

## References

1. Y. Bramoullé and R. Kranton, “Public goods in networks,” *Journal of Economic Theory* 135 (2007), 478–494. First public online date: 28 September 2006. DOI: 10.1016/j.jet.2006.06.006.
2. P. Naghizadeh and M. Liu, “Provision of Public Goods on Networks: On Existence, Uniqueness, and Centralities,” arXiv:1604.08910 (2016).
