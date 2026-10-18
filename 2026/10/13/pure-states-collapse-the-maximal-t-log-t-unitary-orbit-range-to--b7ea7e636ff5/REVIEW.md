# Independent mathematical audit

## correctness

PASS

For any rank-one projectors P and Q=U*PU on Hilbert dimension >=2, if Q=P, maximal f-divergence with f(t)=t log t is 0. If Q differs, c=Tr(PQ)<1 and the two-outcome channel measuring Q and I-Q maps (P,Q) to distributions ((c,1-c),(1,0)), whose classical KL divergence is +infinity. Quantum maximal f-divergence is data-processing monotone, so S_hat_f(P||Q)>=+infinity. Equivalently the f=t log t support criterion fails for any distinct rank-one supports. The orbit image is exactly {0,+infinity} although same/opposite spectral endpoints are 0 and +infinity. Nguyen--Nguyen--Le Corollary 3.3 explicitly asserts for all states the filled interval [0,+infinity], using a continuity argument invalid for rank-deficient Q. Independent exact matrix check for P=diag(1,0), Q=|+><+| gave c=1/2, positive mass 1/2 outside Q. This verifies a counterexample, not the fate of their endpoint theorems.

## originality

PASS

The primary January/February 2026 paper was inspected at Corollary 3.3 and its continuity proof; the explicit pure-state two-value counterexample is not stated there. General Hiai--Mosonyi maximal-f divergence monotonicity and known Belavkin--Staszewski support pathology are prior inputs; the evaluated contribution is the precise contradiction of the universal orbit-range assertion and a faithful-state boundary. A 2026 published qubit-orbit Resultary theorem explicitly restricts to faithful states and does not cover singular counterexamples.

## value

PASS

This is a motivated correction to an incorrect published all-quantum-states claim: unitary-orbit connectedness cannot imply connected finite/extended-real divergence image across support jumps. The explicit pure-state obstruction identifies the missing faithfulness boundary, without suggesting all spectral extremizers or faithful cases fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
