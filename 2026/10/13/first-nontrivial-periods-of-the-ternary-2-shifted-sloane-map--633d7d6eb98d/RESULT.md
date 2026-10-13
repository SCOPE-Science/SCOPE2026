# First nontrivial periods of the ternary 2-shifted Sloane map

## Finding
Let \(f=S_{2,3}\) be the \(2\)-shifted Sloane map in base \(3\). Thus, if
\[
n=(d_kd_{k-1}\cdots d_0)_3,
\]
then
\[
f(n)=\prod_{i=0}^{k}(d_i+2).
\]

The positive periodic points below \(4096\) are exactly
\[
36,\ 64,\ 72,\ 144,\ 288,\ 1152.
\]
Their orbit structure is
\[
36\mapsto36,
\qquad
144\mapsto144,
\qquad
288\mapsto288,
\qquad
1152\mapsto1152,
\]
and
\[
64\mapsto72\mapsto64.
\]

At the next natural period threshold,
\[
4096\mapsto10368\mapsto4608\mapsto4096,
\]
so \(4096\) has exact period \(3\).

Consequently \(64\) is the least positive non-fixed periodic point of \(S_{2,3}\), and \(4096\) is the least positive periodic point whose exact period is at least \(3\).

## Assumptions and scope
Only positive integers are considered. The map is exactly the shifted digit-product map defined in the cited literature with shift \(t=2\) and base \(b=3\).

The result is an exact finite extremal classification. It does not claim a complete classification of all periodic points of \(S_{2,3}\), and it does not prove that every positive orbit stabilizes.

## Proof
The displayed cycles can be checked directly from ternary expansions:
\[
36=(1100)_3,
\]
so
\[
f(36)=3\cdot3\cdot2\cdot2=36.
\]
Likewise
\[
64=(2101)_3,
\qquad
72=(2200)_3,
\]
and therefore
\[
f(64)=4\cdot3\cdot2\cdot3=72,
\qquad
f(72)=4\cdot4\cdot2\cdot2=64.
\]

The other fixed points below \(4096\) have expansions
\[
144=(12100)_3,
\qquad
288=(101200)_3,
\qquad
1152=(1120200)_3,
\]
which give their own values after multiplying the shifted digits.

For the first period-\(3\) orbit,
\[
4096=(12121201)_3,
\]
\[
10368=(112020000)_3,
\]
and
\[
4608=(20022200)_3.
\]
Multiplying each digit after adding \(2\) gives
\[
f(4096)=10368,\qquad
f(10368)=4608,\qquad
f(4608)=4096.
\]
The three integers are distinct, so the period is exactly \(3\).

It remains to prove minimality. This is a finite statement and is exhausted exactly by the accompanying verifier. For every start
\[
1\le n<4096,
\]
the verifier computes \(f\) directly by repeated Euclidean division by \(3\), follows the orbit until a value repeats, extracts the resulting cycle, and records \(n\) precisely when \(n\) lies on that cycle. Every one of the \(4095\) starts reaches a repeated value within eight iterations; the largest value encountered in the complete census is \(41472\). The resulting periodic-point set is exactly
\[
\{36,64,72,144,288,1152\}.
\]
Hence there is no non-fixed periodic point below \(64\), and there is no periodic point of period at least \(3\) below \(4096\). Together with the direct cycle checks above, this proves both least-value assertions.

## Verification
Run
`python3 verify.py`.

The verifier uses integer arithmetic only. It recomputes the shifted ternary digit product from scratch for each step, exhausts all \(4095\) positive starts below \(4096\), reconstructs every repeated cycle, and independently checks the seven displayed ternary expansions and transitions.

The successful replay prints `VERIFY_OK`, the complete periodic set below \(4096\), the maximum number of steps before a repeat, the largest intermediate value reached, and the period-\(3\) orbit beginning at \(4096\).

## Relationship to prior work
Bonuccelli, Colucci, and de Faria formulate the general cycle-and-fixed-point question for shifted Sloane maps. They state that, beyond trivial cases, they can describe all cycles precisely for shift \(t=1\), while for \(t=2\) their stabilization theorem is conditional on digit-equidistribution conjectures. In particular, their treatment of \(S_{2,3}\) does not list or classify its periodic cycles.

The present result addresses the first natural extremal data of that open cycle-classification problem in the smallest nontrivial shifted ternary case: it gives the complete periodic set up to the first point of period \(3\), identifies the least non-fixed periodic point, and identifies the least point of period at least \(3\).

Targeted searches using the exact map, the values \(64,72,4096,10368,4608\), the phrases “2-shifted Sloane” and “base 3,” and the cycle-classification formulation did not locate these extremal statements in the literature or sequence databases.

## Limitations
The finite exhaustion proves exactly the stated minima and the periodic-point set below \(4096\); it says nothing about how many further cycles exist.

The cited stabilization theorem for \(S_{2,3}\) is conditional on a ternary digit-equidistribution conjecture. No such conjecture is assumed here because the present claim is finite.

A residual originality risk is that these small cycles may have been computed informally without being indexed or published.

## References
1. Gabriel Bonuccelli, Lucas Colucci, and Edson de Faria, “On the Erdős-Sloane and Shifted Sloane Persistence Problems,” arXiv:2009.01114v1, 2 September 2020; Journal of Integer Sequences 23 (2020), Article 20.10.7.
2. Samuel S. Wagstaff, “Iterating the Product of Shifted Digits,” Fibonacci Quarterly 19 (1981), 340–347.
