# Independent Audit — A conditional q-ary mirror band for linear-code weight distributions

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `71b79c420fa0ac3d16bc971da8f6c5dc39220cf1`  
**Audited current source tree:** `71b79c420fa0ac3d16bc971da8f6c5dc39220cf1`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this staged change set is not claimed to be already published.

## Correctness — PASS

PASS. If c has weight w>max{s,2d}, the classical bound that a minimal codeword has weight at most s=n-k+1 makes c nonminimal. Choosing a support-minimal proper codeword u inside supp(c) gives d<=wt(u)<=s; the long-gap condition t>=s-d forces wt(u)=d. Among the d ratios c_i/u_i, one scalar occurs at least rho=ceil(d/(q-1)) times, so y=c-lambda u is nonzero and has d<=wt(y)<=w-rho<=d+t; the same gap forces wt(y)=d. Since supp(c) is contained in supp(u) union supp(y), w<=2d, a contradiction. The high-rate specialization and explicit [5,2,2]_q weight enumerator also check. Exhaustive enumeration of all 2,907 ternary linear subspaces of lengths at most five found 248 applicable gap instances and no violation.

## Originality — PASS

PASS, narrowly scoped. The binary mirror theorem is recent and explicitly uses a binary-only disjoint-support decomposition. The submitted theorem replaces it by a q-ary ratio-pigeonhole cancellation of ceil(d/(q-1)) coordinates under an additional long-gap condition, yielding a quantitative positive nonbinary band. Searches for this local-gap endpoint or an equivalent q-ary statement did not locate a covering result. The minimal-codeword bound and ratio pigeonhole are classical and are not credited as new.

## Scientific value — PASS

PASS. Paired with the negative counterexample to the unmodified extension, this gives a concrete sufficient condition under which a q-ary mirror phenomenon survives and quantifies exactly how much cancellation is guaranteed. The extra hypothesis can be strong, but the theorem is a useful structural replacement rather than a finite observation.

## Independent checks

- Reconstructed the support-minimal-codeword proof and checked the nonzero condition for y.
- Checked the endpoint algebra and the high-rate reduction s<=2d.
- Verified the [5,2,2]_q counterexample enumerator directly.
- Exhaustively enumerated all ternary subspaces of length at most five and found no counterexample among every applicable long-gap instance.
- Compared the result with He 2026 and the Ashikhmin--Barg minimal-vector bound.
- Verified no assigned-path file changed between the dispatcher source-check commit and current audited main.

## Limitations

- The added condition t>=n-k+1-d may be restrictive, and the guaranteed interval can be empty for shorter gaps.
- No optimality is claimed for the hypothesis or for the endpoint d+t+ceil(d/(q-1)).
- The construction does not subsume the stronger binary theorem.

## Evidence and references

- https://arxiv.org/abs/2609.20344
- https://doi.org/10.1109/18.705584
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/qary-long-gap-mirror-band--69c27f4f7824

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
