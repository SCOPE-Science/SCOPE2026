# Independent Audit — Nonbinary counterexamples to the literal mirror-vanishing extension

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `58841eb74cb0752c528c8d145bc85e6b30ea4045`  
**Audited current source tree:** `58841eb74cb0752c528c8d145bc85e6b30ea4045`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this staged change set is not claimed to be already published.

## Correctness — PASS

PASS. For the balanced list c_1,...,c_d in F_q^*, the vector v has weight d, while every codeword alpha u+beta v with alpha nonzero retains all d+1 tail coordinates and can cancel at most m=ceil(d/(q-1)) of the first d coordinates. Hence its weight is at least 2d+1-m=d+t+1, proving minimum distance d and the complete gap A_{d+1}=...=A_{d+t}=0. Scalar multiples of u have full weight 2d+1, and k=2=n-2d+1. Counting multiplicities of the balanced c_i also reproduces the stated exact weight enumerator. An independent enumeration over prime fields q=3,5,7,11 and d=2,...,11 reproduced every claimed gap and full-weight witness.

## Originality — PASS

PASS, narrowly scoped. He's September 2026 theorem is binary and its public statement rests on a binary disjoint-support property; the paper notes that larger alphabets require additional conditions. The elementary two-dimensional family here is not claimed as a new code construction, but it supplies an all-q>2, all-d>=2 counterexample satisfying the literal binary-style hypotheses themselves, with arbitrarily long initial gaps. Targeted searches for q-ary mirror-vanishing counterexamples or this parameterized [2d+1,2,d]_q gap family did not locate the same result.

## Scientific value — PASS

PASS. The construction decisively settles the most literal nonbinary extension in the negative for every finite field q>2 and identifies the cancellation mechanism distinguishing q=2. The arbitrarily long gap shows the obstruction is structural rather than a small-parameter accident.

## Independent checks

- Re-derived the weight lower bound for all alpha,beta cases and verified t>=1 for every q>2,d>=2.
- Re-derived the exact enumerator from balanced multiplicities d=a(q-1)+b.
- Independently enumerated the constructed codes for q=3,5,7,11 and d=2 through 11.
- Compared the result with He's binary mirror theorem and the classical Ashikhmin--Barg minimal-vector setting.
- Verified no assigned-path file changed between the dispatcher source-check commit and current audited main.

## Limitations

- The underlying dimension-two codes are elementary and may occur in older code catalogues; novelty is claimed only for the mirror-vanishing counterexample family and interpretation.
- The theorem disproves the literal q-ary extension, not every possible q-ary theorem with stronger hypotheses.
- The motivating binary preprint is very recent, leaving residual simultaneous-work risk.

## Evidence and references

- https://arxiv.org/abs/2609.20344
- https://doi.org/10.1109/18.705584
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/qary-counterexamples-mirror-vanishing--7d5d46a2a226

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
