# Independent mathematical audit

## correctness

PASS

Cloitre Proposition 4.3 directly establishes the complement word w=0 product_h(W_h^(x-2)1), W_(h+1)=W_h^k 1. The discrepancy k*zeros-(k-1)*length has total 1 on every W_h and every prefix lies in [1,1+h(k-1)]. On a uniformly sampled complete word, with probability 1-O(k^(-r)), the first h-r recursive child positions are independent uniform 0..k-1 digits; the remainder is O(r), r=floor(h^(1/3)). Classical i.i.d. CLT yields mean (k-1)h/2 and variance (k^2-1)h/12. The stage partition of a uniform global index discards o(N) letters and replaces every good position by a uniform W_m prefix with bounded O(H^(1/3)) deviation and global stage drift (x-k-1)H. Combining yields center (x-2-(k-1)/2)log_k N and the asserted nonzero Gaussian scale for all fixed k>=2,x>=3. Independently checked the word/sequence equivalence for 5 parameter pairs at lengths 2047-3000; these finite words do not establish the CLT.

## originality

PASS

No dominating equivalent or stronger complete statement identified in the targeted primary-source and Resultary searches; assessment is best-of-knowledge, not exhaustive priority certification. Exact sequence description determines values but is not equivalent to an already stated/proved Gaussian limit without a new asymptotic analysis. Known digit-sum formulas may imply the special x=k+1 subcase using standard CLT, but inspected texts do not establish the full arbitrary-x stage-boundary theorem. An exact sequence table is not itself a table of the normalized weak limit; no matching law found in the specific indices checked. New proof requires independent child-digit coupling, negligible root/boundary events and the stage drift, none asserted as a stronger limiting result in inspected primary HTML.

## value

PASS

An explicit second-order logarithmic-drift central limit law at uniformly chosen indices is a motivated statistical refinement of existing exact deterministic tree words and first-order densities, valid for all fixed initial values x and branching k. It isolates the initial-condition drift from universal variance and requires nontrivial control of stage boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
