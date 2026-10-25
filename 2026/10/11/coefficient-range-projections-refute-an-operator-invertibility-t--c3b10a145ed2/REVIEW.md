# Scientific review

## Correctness — PASS

The published Theorem 4.2 is false as stated. With all coefficient spaces equal to H=R^2 and K=I, the two nonzero operators Lambda_1=[[1,0],[0,0]] and Lambda_2=[[0,1],[0,0]] satisfy sum Lambda_j^*Lambda_j=I. The rank-one projection T=diag(1,0) fixes every coefficient operator under postcomposition, so the original and both transformed families are Parseval K-g-frames, while TT*=T is singular. All identities hold equally over C^2.

The same obstruction applies whenever the closure of the coefficient-range span is proper: projection onto that closed span is invisible to all coefficient outputs. A restricted sufficient repair is obtained when the ordinary g-frame analysis operator is surjective onto its full coefficient direct sum; transformed lower bounds then force both T and T* to be bounded below, hence T is invertible. This is not claimed to repair the general theorem.

## Originality — PASS (best of knowledge)

Kiran Kumar and Upender Reddy's 2020 Theorem 4.2 is the exact claim being corrected. Ramu and Johnson's 2016 Theorem 3.7 proves the analogous assertion for transformed **frame vectors**, whose analysis coefficients test T* throughout the ambient space. That proof does not imply the statement for left-postcomposed operator-valued coefficient maps.

Published results about right composition by T, generalized fusion-frame adjoint-range conditions, and compression of K-frame operators concern different mathematical transformations. They were checked at the level of full available mathematical statements. No independently indexed source containing this exact theorem-specific projection correction was located. The earlier Hua--Huang K-g-frame stability paper could be inspected only at its abstract and bibliographic record; an unindexed prior correction remains a real priority risk.

## Mathematical value — PASS

The example invalidates a global operator-invertibility theorem under exceptionally transparent Parseval and identity-K hypotheses. More importantly, it identifies the structural reason the extension from vectors to coefficient operators fails: postcomposition may leave all coefficient observations unchanged on a proper output subspace. The counterexample and restricted repair are directly useful for interpreting or correcting this theorem. No broad characterization is claimed.

## Scope and limitations

The failure concerns Theorem 4.2, not every other result in the original paper. The coefficient-range spanning condition is necessary for this universal left-postcomposition implication but not proven sufficient. The stronger sufficient repair requires an onto ordinary g-frame analysis operator. Formal proof-assistant and expert-attestation channels are not asserted.

## Primary references

- N. Kiran Kumar and G. Upender Reddy, *Operators Preserving K-g- Frames*, Turkish Journal of Computer and Mathematics Education 11(3) (2020), 1462–1468, Theorem 4.2. DOI: 10.17762/turcomat.v11i3.12958.
- G. Ramu and P. Sam Johnson, *Frame operators of K-frames*, SeMA Journal 73 (2016), 171–181, Theorem 3.7. DOI: 10.1007/s40324-016-0062-4.
- D. Hua and Y. Huang, *K-g-Frames and Stability of K-g-Frames in Hilbert Spaces*, J. Korean Math. Soc. 53(6) (2016), 1331–1345. DOI: 10.4134/JKMS.j150499.
