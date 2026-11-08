# Independent mathematical audit

## correctness

PASS

The lifted Markov state is (Xt,Xt-1), transitions (a,b)→(x,a) with q_ab∈(0,1). Stationary equal pair probabilities p01=p10=s imply π0=A/(A+B),π1=B/(A+B). First-positive-passage recurrences h1=1+(1−q_ab)h1(0,a), h0=1+q_ab h0(1,a) solve to displayed 4×2 tables; weighted differences factor exactly π1(u−v)^2/u and π0(w−z)^2/(1−z). Positivity makes both zero iff u=v and w=z. Conversely first-order Kemeny identity yields 1+1/(u+1−w), verified by substitution. Independently solved rational sample (u,v,w,z)=(1/2,1/4,1/2,3/4) obtaining θ=(49/22,95/44,57/22,119/44), defects (3/44,5/44). Input verify.py separately solves the stationary and two hitting linear systems; no extension to nonpositive boundary tensors.

## originality

PASS

Qualified best-of-knowledge originality: Kemeny constancy for a genuine Markov chain supplies sufficiency when u=v,w=z; no converse for a non-Markov one-time observation follows unless the two quadratic defects are proved. No exactly covering theorem was found in actual indexed results or the inspected relevant primary statements; this is not a historical priority certificate.

## value

PASS

This answers a specific open rigidity question for the smallest nontrivial higher-order Markov model: constancy of stationary-target first-positive hitting time forces genuine first-order memorylessness, with sharp explicit nonnegative quadratic defects. Its condition is not implied by classical Kemeny constancy without proving the converse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
