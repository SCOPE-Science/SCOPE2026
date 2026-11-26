# Independent mathematical audit

## correctness

PASS

For a signed input use g=U_R|f| and V(|f|)≤V(f). In the nonnegative proof, an interval witnessing a local-maximum plateau height H cannot leave the plateau: the same admissible interval would give its outside neighboring vertex a value at least H. Inside, every input entry is at most H, so a witnessing average of H supplies a contact point p with f(p)=g(p)=H. Removing flat segments at the ends and decomposing the remaining changes into adjacent peak/valley monotone segments charges disjoint input edges, with each vertical drop at most V(f;[p,v]) by g(v)≥f(v). For R=n the interval joining p and v is itself admissible at v; with d=|p−v| and m its minimum input value, the drop is at most d(H−m)/(d+1)≤(n−1)V(f;[p,v])/n. This also covers boundary peaks and n=2; constant outputs require no charging. The endpoint indicator has output 1/i for i≤R and zero later, so its telescoping variation gives equality for both regimes. Independently tested 38,233 signed integer profile/horizon pairs and 27 endpoint witnesses (lengths 2–7, integer-LCM scaling, no tolerance); replay node /workspace/review-evidence/4.js. The tests supplement RESULT.md lines 24–57, not a universal proof. Frozen verifier read but not executed.

## originality

PASS

The supported distinct finding is the finite sharp horizon transition, specifically the strict full-horizon factor and its sharp discontinuity at admitting the longest interval. The peak-contact argument and nonincrease alone have antecedents; the comparison does not credit those as distinct stand-alone results. The strongest inspected apparent identical constant is for a centered operator, or for other input seminorms, not for this one-input interval operator.

## value

PASS

This is a sharp cutoff for a natural finite smoothing operator, rather than an isolated numerical gain. It quantifies precisely when the standard nonincrease becomes strict, and shows that dropping just the one longest interval removes the strict improvement. The local estimate explains the role of full access and the same input attains both regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
