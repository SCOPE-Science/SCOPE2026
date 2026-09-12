# Disproof of the prime-field Cartesian-grid N^{3/2-1/12} point–plane bound

## Context

Let p be prime and P = A x B x C subset F_p^3 with |A|=|B|=|C|=t, m=|P|=t^3, and Pi a set of n=m=:N planes with N <= p^{3/2}. The target claim asked whether absolute C>0 and delta=1/12 exist with I(P,Pi) <= C N^{3/2-delta} for all such configurations, provable via polynomial partitioning with ruled-surface analysis, or else an explicit infinite family with I(P,Pi)/N^{3/2-delta} unbounded. This is a TARGET two-sided question; a rigorous disproof is a complete resolution.

## Definitions

Incidences I(P,Pi)=|{(q,pi) in P x Pi : q in pi}|. Put 3/2-delta=17/12. For integer s>=20 let t=s^2, N=t^3=s^6, dmax=3s(t-1)=3s^3-3s, D=dmax+1. Let p>=s^4 be prime. Let A=B=C={0,...,t-1} in F_p, P=A x B x C. Let S={(a,b,c) in {1,...,s}^3 : gcd(a,b,c)=1} and Pi_0={ax+by+cz=d : (a,b,c) in S, d in {0,...,dmax}}. Let Pi be the N planes of Pi_0 with largest |P cap pi|.

## Result

The uniform bound is false. For the above infinite family, |Pi|=N, N<=p^{3/2}, all planes are distinct mod p, and

I(P,Pi) >= N^2/D >= N^{3/2}/3,

so I(P,Pi)/N^{17/12} >= N^{1/12}/3 = s^{1/2}/3 -> infinity as s->infinity. Hence no absolute C satisfies I<=C N^{17/12} uniformly. For example s=100 already gives ratio >=10/3.

## Proof / Evidence

Preconditions: t=s^2<s^4<=p; dmax=3s^3-3s<s^4<=p for s>=3; N=s^6<=(s^4)^{3/2}<=p^{3/2}.

Primitive count: by Mobius inversion |S|=sum_{d<=s} mu(d) floor(s/d)^3 >= s^3/zeta(3)-s/2-(pi^2/2)s^2 >= s^3/2 for s>=20, using zeta(3)<1.21 and 1/zeta(3)>0.826.

Width: D=3s^3-3s+1 satisfies 2s^3<=D<=3s^3, so n_0=|S| D>=s^6=N and top-N selection is possible.

Distinctness mod p: if two indexed planes coincided in F_p^3, normals v,w would satisfy v x w=0 in F_p^3 with each coordinate an integer of absolute value <=s^2-1<s^4<=p, hence zero over Z; primitivity with positive entries forces v=w, and then d=d' in F_p with values in [0,dmax], dmax<p, forces d=d'. So all n_0 planes are distinct.

Counting: for fixed v in S and x in P, v.x=ax+by+cz lies in [0,dmax] as integers, below p, so reduction mod p is faithful; each grid point lies on exactly one plane of direction v in Pi_0. Hence sum_{pi in Pi_0}|P cap pi|=N|S|. Top-N averaging gives I(P,Pi)>=(N/n_0)N|S|=N^2/D>=N^{3/2}/3 since D<=3s^3=3N^{1/2}. Dividing by N^{17/12} yields ratio >=N^{1/12}/3.

Computation: output/artifacts/verify_counterexample.py exactly enumerates s=2 (N=64, top-64 incidences 395, ratio ~1.09) and s=3 (N=729, incidences 16137, ratio ~1.42), checking preconditions, partition identity, distinctness, and averaging. Divergence for large s is analytic.

## Limitations

Disproves only the uniform N^{3/2-1/12} bound. Does not rule out a weaker uniform bound C N^{3/2-delta'} with smaller delta', a bound with C growing slowly in p, or bounds under extra restrictions on Pi. Exact enumeration covers s=2,3; large-s divergence rests on proved estimates.

## Reproducibility

Run `python3 output/artifacts/verify_counterexample.py`. No extra dependencies beyond Python 3 standard library.

## References

- M. Rudnev, On the number of incidences between points and planes in three dimensions, arXiv:1407.0426.
- F. de Zeeuw, A short proof of Rudnev's point-plane incidence bound, arXiv:1612.02719.
- M. Rudnev, Point-plane incidences and some applications in positive characteristic, arXiv:1806.03534.
