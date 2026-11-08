# Independent mathematical audit

## correctness

PASS

For finite known nonempty S,T and arbitrary order of unit items of exactly these two types, assume s=|S|<=t=|T| and label k common agents u_p by p=1..k in the S-order. Assign each u_p position q(p)=floor(t(1-p/s))+1 in the T-order; q values strictly decrease at least one each and 1<p/s+q/t<=1+1/t. Two independent cyclic assignment sequences then give shared load L=A+B+1_{r>=p}+1_{v>=q} for type counts a=As+r, b=Bt+v. If both indicators vanish, r/s+v/t<1; if both one, the fractional remainder exceeds 1; if exactly one, integer one lies between floor and ceiling for fractional remainder in (0,2). All nonshared agents get regular round-robin quota, others zero. Therefore both global floor/ceiling quotas hold at each prefix against adaptive arrivals, with no future knowledge. Independently checked 249900 exact residue configurations for s<=t<=14 and every feasible shared intersection. p,s=1 boundary and identical S=T included; Prop1 good/chores as stated follows for unit valuations but is weaker than quota.

## originality

PASS

Cembrano–Correa–Griesbach–Verdugo (arXiv:2510.14752v1) explicitly proves no online global quota algorithm for arbitrary incoming vote vectors if n>=4. Here the input alphabet is only two fixed uniform-support vectors, so its adversarial impossibility example uses three or more distinct vectors and does not contradict or imply this construction. Biburger–Megow–Shahkarami (arXiv:2610.08064) studies unrestricted eligibility sequences and approximations for Prop1, not an exact two-support global quota formula in its abstract. The explicit antipodal cycle phase matching for overlapping supports is an additional constrained-alphabet construction. Historical equivalent two-color fair scheduling or rounding results remain a genuine risk.

## value

PASS

Online two-eligibility-type allocation is a natural threshold between trivial one-type round robin and unrestricted adversarial impossibility. The algorithm gives simultaneous upper/lower quota for arbitrarily many agents and crossing sets without reassignment. This identifies a mathematically meaningful tractable input alphabet with a concise constructive invariant; it is not merely ordinary one-type round robin because shared agents require a coupled phase design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
