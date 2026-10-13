# The published \(\mathsf{ITL}^e\) finite-model bound has linear tower height

## Finding
Let \(B(s)\) be the explicit finite-model bound in Lemma 30 of Boudou, Diéguez, and Fernández-Duque's 2017 paper *A Decidable Intuitionistic Temporal Logic*. Define
\[
T_0(x)=x,\qquad T_{h+1}(x)=2^{T_h(x)}.
\]
Then, for every integer \(s\ge1\),
\[
\boxed{
T_{s+2}(2^{s+1})\;\le\;B(s)\;\le\;T_{s+3}(3\cdot2^{s+1}).
}
\]
Consequently, for the base-two iterated logarithm
\[
\log_2^*x=\min\{m:\log_2^{(m)}x\le1\},
\]
one has
\[
\boxed{
\log_2^* B(s)=s+\log_2^*s+O(1).
}
\]
Thus the *published construction itself* has tower height asymptotic to the formula size with leading coefficient one. This sharpens the paper's qualitative statement that its decision procedure is non-elementary: its displayed bound is non-elementary but still lies on a linear-height exponential-tower scale, rather than at an Ackermannian or more rapidly growing scale.

## Assumptions and scope
The statement concerns only the explicit function \(B(s)\) proved in the 2017 paper. It does **not** claim that the smallest countermodel for an \(s\)-symbol formula has this size, nor that validity or satisfiability for \(\mathsf{ITL}^e\) has a matching lower complexity bound.

The source defines, for integers \(n,k\ge0\),
\[
E_0^n=0,\qquad E_{k+1}^n=E_k^n+n2^{E_k^n},
\]
\[
Q_0^n=0,\qquad Q_{k+1}^n=1+E_k^nQ_k^n,
\]
and Lemma 30 gives
\[
B(s)=Q_{s+3}^{2^{s+1}}
\left(
2E_{s+1}^{2^s}
+sQ_{s+1}^{2^s}E_{s+3}^{2^{s+1}}
\right).
\]
Here the superscripts on \(E\) and \(Q\) are parameters, not powers.

## Proof
Fix \(n\ge2\). First, the \(E\)-recurrence has a one-tower-step lower bound:
\[
E_k^n\ge T_{k-1}(n)\qquad(k\ge1),
\]
because \(E_1^n=n\) and \(E_{k+1}^n\ge2^{E_k^n}\).

For the upper bound, put \(D_k=T_{k-1}(3n)\). We prove
\[
E_k^n\le \frac{D_k}{2}.
\]
The base case is \(n\le3n/2\). If \(E_k^n\le D_k/2\), then
\[
E_{k+1}^n
=E_k^n+n2^{E_k^n}
\le(n+1)2^{E_k^n}.
\]
For \(n\ge2\),
\[
\log_2(n+1)\le\frac{3n}{2}-1\le\frac{D_k}{2}-1,
\]
so
\[
E_{k+1}^n\le2^{D_k-1}=\frac{D_{k+1}}2.
\]
Hence
\[
T_{k-1}(n)\le E_k^n\le\frac12T_{k-1}(3n).
\]

The same tower height controls \(Q\). Since \(Q_1^n=1\), suppose \(Q_k^n\le D_k\). Using the preceding estimate,
\[
Q_{k+1}^n=1+E_k^nQ_k^n\le1+\frac{D_k^2}{2}\le2^{D_k}=D_{k+1},
\]
where the elementary inequality \(1+D^2/2\le2^D\) holds for \(D\ge6\), and here \(D_k\ge3n\ge6\). Thus
\[
Q_k^n\le T_{k-1}(3n).
\]

Now set \(N=2^{s+1}\). The large \(E\)-factor in \(B(s)\) gives
\[
B(s)\ge E_{s+3}^{N}\ge T_{s+2}(N).
\]
For the other direction, every \(E\)- or \(Q\)-factor appearing in \(B(s)\) is at most
\[
X=T_{s+2}(3N).
\]
Therefore
\[
B(s)\le X(2X+sX^2).
\]
For \(s\ge1\), this \(X\) is much larger than both \(32\) and \(s+2\), so
\[
X(2X+sX^2)\le X^5\le2^X=T_{s+3}(3N).
\]
This proves the displayed tower sandwich.

Finally, for \(x>1\),
\[
\log_2^*T_h(x)=h+\log_2^*x.
\]
Applying this to the two sides gives the explicit bracket
\[
s+3+\log_2^*(s+1)
\le \log_2^*B(s)
\le s+4+\log_2^*(s+1+\log_2 3),
\]
which is equivalent to
\[
\log_2^*B(s)=s+\log_2^*s+O(1).
\]

## Verification
`verify_tower_height.py` replays the source recurrences on manageable exact instances, checks the lower and upper tower inequalities wherever the towers remain constructible, verifies the two elementary induction inequalities on broad integer ranges, and checks the exact identity \(\log_2^*T_h(x)=h+\log_2^*x\) on feasible towers. It returns a deterministic `VERIFY_OK` line.

The script is only a transcription and boundary check. The all-\(s\) result is established by the symbolic inequalities in the proof.

## Relationship to prior work
Boudou, Diéguez, and Fernández-Duque define the recurrences \(E_k^n,Q_k^n\), give the explicit \(B(s)\), prove the strong finite-model property, and explicitly remark that their resulting decision procedure is non-elementary while leaving open whether the logic admits an elementary bound after further trimming. The inspected source does not quantify the tower height of \(B(s)\).

Targeted searches for the exact recurrence, the bound \(B(s)\), “tower height,” and iterated-log formulations did not locate a published equivalent of the displayed sandwich or the asymptotic \(\log_2^*B(s)=s+\log_2^*s+O(1)\). The contribution here is therefore a quantitative analysis of the *published upper bound*, not a new decidability theorem.

## Limitations
This result does not settle the complexity of \(\mathsf{ITL}^e\). In particular, it supplies no non-elementary lower bound on the logic itself and does not rule out the source authors' suggestion that a different construction might yield elementarily bounded models. The originality risk is that this short recurrence analysis may be known informally but uncatalogued.

## References
1. Joseph Boudou, Martín Diéguez, and David Fernández-Duque, “A Decidable Intuitionistic Temporal Logic,” CSL 2017, LIPIcs 82, Article 14, DOI: 10.4230/LIPIcs.CSL.2017.14; arXiv:1704.02847.
2. Somayeh Chopoghloo and Morteza Moniri, “A strongly complete axiomatization of intuitionistic temporal logic,” *Journal of Logic and Computation* 31(7), 2021, 1640–1659, DOI: 10.1093/logcom/exab041.
