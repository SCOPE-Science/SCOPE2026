# Review

## Correctness
PASS. The matrices
\[
T=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix},
\qquad
K=I-T
\]
satisfy
\[
T^2=T,\qquad TK=KT=0.
\]
The singleton \(\psi=(-1,1)\) is an exact Parseval \(K\)-frame because
\[
|\langle x,\psi\rangle|^2=\|K^*x\|^2
\]
for every \(x\). Yet \(T\psi=0\), while \(K^*e_1\ne0\) for \(e_1\in R(T)\), so the transformed family has no lower \(K\)-frame bound.

The Moore--Penrose inverse gives
\[
TT^\dagger=P_{R(T)},
\]
which kills \(K^*e_1\). This exactly identifies the invalid step in the published proof.

## Originality
PASS. The exact source, theorem number, transformed-frame statement, Moore--Penrose formulation, oblique-projection formulation, and \(K^*\)-range-invariance formulation were searched and implication-compared.

A distinct result concerning the neighboring Theorem 3.6 uses an isometry/co-isometry obstruction. It does not imply this closed-range idempotent counterexample. The closest indexed \(K\)-frame findings concern compression, scaling, excess, or perturbation and do not subsume the claim.

## Value
PASS. The theorem asserts invariance of a controlled \(K\)-frame under a broad closed-range transformation. The stated hypotheses can instead send an exact Parseval \(K\)-frame to zero. The repair identifies the missing range geometry rather than merely changing a numerical constant.

## Limitations
The added condition
\[
K^*(R(T))\subseteq R(T)
\]
is a direct sufficient repair for the published argument, not claimed to be the weakest possible condition. The finding does not reassess neighboring theorems.

Same-model review: passed. Independent audit: not yet performed.
