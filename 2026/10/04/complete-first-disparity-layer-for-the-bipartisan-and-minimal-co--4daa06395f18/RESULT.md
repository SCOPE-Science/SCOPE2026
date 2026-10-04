# Complete first disparity layer for the bipartisan and minimal covering sets
## Finding
For a finite tournament \(T\), the **bipartisan set** \(BP(T)\) is the support of the unique maximal lottery, equivalently the support of the unique symmetric Nash equilibrium of the associated zero-sum tournament game.

A nonempty subset \(B\) is a **covering set** if every alternative \(x\notin B\) is covered by some member of \(B\) in the subtournament induced by \(B\cup\{x\}\). The **minimal covering set** \(MC(T)\) is the unique inclusion-minimal covering set.

It is known that
\[
BP(T)\subseteq MC(T)
\]
for every tournament, and prior exhaustive work established the disparity index
\[
d(BP,MC)=6.
\]

The complete first disparity layer is:

\[
\#\{T:\ |T|=6,\ BP(T)\ne MC(T)\}=1440.
\]

Since there are
\[
2^{\binom 62}=2^{15}=32768
\]
labeled tournaments on six alternatives, the exact uniform incidence is
\[
\frac{1440}{32768}=\frac{45}{1024}.
\]

Every strict case has
\[
|BP(T)|=5
\qquad\text{and}\qquad
MC(T)=A,
\]
where \(A\) is the six-element alternative set.

Moreover, the \(1440\) strict tournaments form exactly two isomorphism classes. Each class has labeled orbit size
\[
720=6!,
\]
so both canonical tournaments have trivial automorphism group.

Using alternatives \(A,B,C,D,E,F\), one canonical class has out-neighborhoods
\[
\begin{aligned}
A&\to\{E,F\},&
B&\to\{A,D,F\},&
C&\to\{A,B\},\\
D&\to\{A,C\},&
E&\to\{B,C,D\},&
F&\to\{C,D,E\}.
\end{aligned}
\]
For this class,
\[
BP(T)=\{A,B,C,E,F\},
\qquad
MC(T)=\{A,B,C,D,E,F\},
\]
and the unique maximal lottery is
\[
p=\left(\frac15,\frac15,\frac15,0,\frac15,\frac15\right).
\]
Its payoff vector against pure columns is
\[
p^{\mathsf T}G(T)=\left(0,0,0,\frac15,0,0\right).
\]

The second canonical class has
\[
\begin{aligned}
A&\to\{B,E,F\},&
B&\to\{D,F\},&
C&\to\{A,B\},\\
D&\to\{A,C\},&
E&\to\{B,C,D\},&
F&\to\{C,D,E\}.
\end{aligned}
\]
Here
\[
BP(T)=\{A,B,D,E,F\},
\qquad
MC(T)=\{A,B,C,D,E,F\},
\]
with maximal lottery
\[
p=\left(\frac13,\frac19,0,\frac13,\frac19,\frac19\right)
\]
and payoff vector
\[
p^{\mathsf T}G(T)=\left(0,0,\frac19,0,0,0\right).
\]

Thus the first point at which the weak-saddle solution \(MC\) expands beyond the equilibrium-support solution \(BP\) is highly rigid: it always adds exactly one alternative, and there are only two unlabeled types.

## Assumptions and scope
A tournament is a complete asymmetric directed graph. The tournament game uses skew-adjacency entries \(1\) for a win and \(-1\) for a loss.

The bipartisan set is the support of the unique maximal lottery. The minimal covering set uses the standard covering relation inside \(B\cup\{x\}\) for each excluded alternative \(x\).

The equality statement through five alternatives and the existence of a six-alternative counterexample are prior results. The new claim is the complete labeled and unlabeled classification of the first disparity layer.

No claim is made about disparity frequencies for seven or more alternatives.

## Proof
The verifier exhausts every labeled tournament of orders \(1\) through \(6\).

For the bipartisan set, the primary computation exploits the odd support of a maximal lottery in a skew-symmetric tournament game. For each odd candidate support \(S\), an exact integer null vector is constructed from Pfaffians of the even principal minors. A support is accepted exactly when the null vector is strictly positive and its induced mixed strategy has nonnegative payoff against every pure alternative.

For the minimal covering set, every nonempty subset is tested directly for external covering stability. All inclusion-minimal covering sets are then computed; exactly one occurs in every tournament.

The resulting histograms show no disparity for orders \(1,\ldots,5\). At order \(6\),
\[
\begin{array}{c|r}
(|BP|,|MC|,\text{equal?}) & \text{count}\\ \hline
(1,1,\text{yes}) & 6144\\
(3,3,\text{yes}) & 20480\\
(5,5,\text{yes}) & 4704\\
(5,6,\text{no}) & 1440.
\end{array}
\]

Hence every strict case has \(BP\) of size \(5\) and \(MC\) equal to the full tournament.

As an independent check of the covering-set computation, Brandt's iterative polynomial-time algorithm is replayed on every tournament through order \(5\) and on every one of the \(1440\) strict order-\(6\) tournaments.

As an independent check of the maximal lotteries on the entire strict layer, exact rational Gaussian elimination is replayed for all \(1440\) strict tournaments and agrees with the Pfaffian computation.

Finally, every strict tournament is canonicalized under all \(6!\) relabelings. Exactly two canonical bit encodings occur:
\[
344
\quad\text{and}\quad
345,
\]
each exactly \(720\) times. Direct rational replay gives the two lotteries and payoff vectors displayed above.

## Verification
The embedded `verify_bp_mc_first_layer.py` uses only the Python standard library and exact arithmetic.

It verifies:
- every tournament of orders \(1\) through \(6\);
- \(BP(T)\subseteq MC(T)\) throughout the domain;
- equality for all tournaments through order \(5\);
- the complete order-\(6\) histogram;
- exactly \(1440\) strict cases and probability \(45/1024\);
- strict size pair \((5,6)\) in every divergent case;
- Brandt-algorithm replay of \(MC\) on all lower-order tournaments and all strict order-\(6\) cases;
- rational-Gaussian replay of the maximal lottery on all \(1440\) strict cases;
- exactly two isomorphism classes, each with orbit size \(720\);
- the two displayed canonical lotteries and payoff vectors.

Run:

`python3 verify_bp_mc_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Laffond, Laslier, and Le Breton introduced the bipartisan set as the support of the unique equilibrium of a tournament game. Later tournament-solution work records the general inclusion
\[
BP(T)\subseteq MC(T).
\]

Brandt's tournament-solution framework gives both the equilibrium-support formulation of \(BP\) and an algorithm for computing \(MC\) that starts from \(BP\).

Brandt, Dau, and Seedig studied disparity and separation indices systematically. Their exhaustive analysis establishes that a tournament of order \(6\) is minimal for \(MC\ne BP\) and gives a six-alternative witness in which \(BP\) has five alternatives while \(MC\) is the full set.

The new result does not claim that threshold or that witness. It classifies the entire first layer: exactly \(1440\) labeled tournaments, exactly two unlabeled classes, and no other strict size pattern.

Scott and Fey prove that in almost all large tournaments the minimal covering set is the entire alternative set, whereas known random-tournament results put the bipartisan support at roughly half the alternatives. The six-alternative classification therefore identifies the first finite point at which this later large-tournament separation begins.

Targeted searches for the exact count \(1440\), the probability \(45/1024\), and a two-class order-\(6\) classification did not locate an equivalent published table or theorem.

## Limitations
The theorem is a finite first-layer census, not a formula for larger tournament orders.

The disparity index \(6\) is prior work and is not claimed as new.

The two canonical classes are represented by one fixed bit convention in the verifier; the scientific content is invariant under relabeling.

An unindexed data file from earlier exhaustive tournament searches, a thesis appendix, or unpublished computational output could contain the same complete census.

## References
1. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008; later *Journal of Economic Theory* 146(4) (2011), 1481–1499.
2. F. Brandt, A. Dau, and H. G. Seedig, “Bounds on the disparity and separation of tournament solutions,” *Discrete Applied Mathematics* 187 (2015), 41–49. DOI: 10.1016/j.dam.2015.01.041.
3. A. Scott and M. Fey, “The minimal covering set in large tournaments,” *Social Choice and Welfare* 38 (2012), 1–9. DOI: 10.1007/s00355-010-0503-4.
4. G. Laffond, J.-F. Laslier, and M. Le Breton, “The bipartisan set of a tournament game,” *Games and Economic Behavior* 5 (1993), 182–201.
