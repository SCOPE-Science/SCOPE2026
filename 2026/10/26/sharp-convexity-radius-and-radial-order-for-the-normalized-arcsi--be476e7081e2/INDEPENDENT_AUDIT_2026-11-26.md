# Independent mathematical audit

## correctness

PASS

For p=zf'/f=Phi(omega), positivity follows from the arcsine Taylor coefficients, so f is starlike and f' does not vanish. Logarithmic differentiation gives the stated convexity expression. For |z|=r>0, Schwarz–Pick applied to omega(z)/z gives |z omega'−omega|≤(r²−t²)/(1−r²) with t=|omega|, including the constant-modulus equality case by Schwarz's lemma. The coefficient bound gives Re Phi≥D(t)>0 and |Phi'|≤c/sqrt(1−t²), yielding the displayed scalar estimate. For F=arcsin t+B_r(t)/(sqrt(1−t²)D(t)), multiplying F' by sqrt(1−t²)D(t) gives D+1−2t/(1−r²) plus a nonnegative term. On t≤r≤11/20 this is strictly above 3/5−161/279=32/1395, so the estimate is minimized at t=r. Omega=−z realizes every inequality on the positive real radius, including the limiting normalized case r=0. Beta decreases strictly and changes sign in the exact bracket: beta(1/2)=2/3−sqrt(3)/π>0, and at 11/20 the rational bound (21/25)(30353/48000)^2<7/20<cr yields negativity. Independently bisected (2/π)sqrt(1−r²) arccos(r)^2−r, giving R≈0.538585996535522. The real-part convexity criterion gives convexity on the open disk of radius R and the same extremal violates it immediately beyond R. Inspected verify.py without executing it; the radial-order identity is proved only through 11/20, not for all r<1.

## originality

PASS

The exact class, standard derivative estimates and analogous Ma–Minda radius arguments are antecedents. The inspected same-class and neighboring primary and indexed findings do not supply the target-specific sharp radial profile or radius. The exact optimization and common extremizer are the distinct supported result, not a new general subordination inequality.

## value

PASS

For an independently introduced Ma–Minda class, the threshold of guaranteed convexity is a standard useful geometric invariant. The result also gives the exact convexity order, not just a sufficient radius: it determines the worst real part at each radius across an interval containing the transition and supplies one extremizer throughout. The required extremum does not follow from the known sector/image bounds alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
