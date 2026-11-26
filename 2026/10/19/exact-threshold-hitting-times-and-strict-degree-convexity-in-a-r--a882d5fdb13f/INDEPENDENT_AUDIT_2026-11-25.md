# Independent mathematical audit

## correctness

PASS

For a fixed absorbing threshold n, let T_k be the expected time from k and D_k=T_k−T_0. The backward equation for k<n is α(D_{k+1}−D_k)−r[(k+1)D_k−kD_{k−1}]=−1, with no downward term at zero. Summing from 0 through k telescopes to αD_{k+1}=−(k+1)+(k+1)rD_k. With D_0=0 and D_n=−M_n this proves the finite sum and recursion directly, without assuming the renewal identity. Independent reset trials have positive probability of n consecutive births, and trial durations are bounded in mean by 1/r, so the finite expectation is justified. Two falling-factorial differences give the stated positive coefficients and the uniform j=2 lower bound. Reindexing P_n(0) by n−j gives the partial exponential sum and the stated fixed-rate factorial asymptotic. For the transform, the direct discounted backward recurrence, after dividing all state values by the value at zero, has initial values W_0=1,W_1=1+s/α and recurrence W_{k+1}=[1+(s+(k+1)r)/α]W_k−krW_{k−1}/α−r/α. Substitution verifies W_k=(sP_k(s)+r)/(s+r); imposing the terminal value at n gives the stated transform, including s=0. The displayed means at α=2,r=1/2 agree with the recurrence.

## originality

PASS

The supported distinct contribution is the solved exact matched-rate degree-threshold mean and its uniform strict integer-target curvature for the process left to continuum approximation by Artime. Neither the catastrophe process nor the generic reset renewal identity is credited as new.

## value

PASS

The exact integer-target profile supplies both a finite computable mean and a definitive test of the continuum curvature interpretation in the model that prompted the question. The strict bound on ordinary second differences rules out a rate-dependent curvature transition for every integer target, not just low-degree examples or asymptotic data. The explicit matched-rate simplification and factorial growth also give useful benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
