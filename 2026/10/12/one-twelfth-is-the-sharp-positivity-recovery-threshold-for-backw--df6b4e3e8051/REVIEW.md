# Independent mathematical audit

## correctness

PASS

Define W=(S^-1+10I+S)/12 and D=S^-1-2I+S on the bi-infinite lattice; sigma>=0, A=W-sigma D has center a=5/6+2sigma and neighbors b=1/12-sigma. For sigma=0, B=A^-1 W=I. If sigma>=1/12 then b<=0 and a-2|b|=1, so inverse Green kernel of A is nonnegative; multiplying by W>=0 shows B>=0 and since B1=1 preserves all constant-bound data ranges. If 0<sigma<1/12, A^-1 kernel is C r^|j| with C=(a²-4b²)^-1/2>0 and -1<r<0; using b(r²+1)+ar=0 yields (B e0)_2=-12*C*sigma*r²/(1-12sigma)<0. This proves exact iff for the infinite lattice. Independently verified four-cycle at sigma=1/100: [13217/13568,3/212,-33/13568,3/212], whose sum is 1 and third component is negative. This finite witness only refutes unqualified finite-periodic positivity, not an all-size threshold.

## originality

PASS

The earlier compact scheme paper studies precisely W,D and describes a maximum-principle expectation for backward Euler without the positive-time restriction, but its main formal results concern explicit weak monotonicity, limiters, and related spatial discretizations. General lower timestep positivity effects and filtered Crank–Nicolson do not determine this sharp compact backward-Euler threshold. The exact if-and-only-if and counterexample under the same spatial operator survive as a distinct claim.

## value

PASS

High-order compact heat discretizations can be stable but fail pointwise positivity, a substantive issue for maximum principles. The exact nonmonotone (re-entrant) timestep cutoff and rigorous counterexample correct a plausible unconditional assertion, giving a useful sharp condition rather than a routine M-matrix sufficient bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
