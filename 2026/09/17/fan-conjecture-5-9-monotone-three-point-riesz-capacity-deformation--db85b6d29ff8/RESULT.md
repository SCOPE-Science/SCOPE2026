# Fan Conjecture 5.9: monotonicity of the three-point Riesz-energy deformation

> **Correction notice.** This stable record originally contained a preliminary Non-Cancelling Intersections result from the same run. the same-model review's corrected final report invalidated that preliminary result as this run's accepted SCOPE outcome after prior-run history revealed a cross-run independence conflict. See `CORRECTION.md`. The mathematical NCI draft is retained separately as negative research memory, not as an accepted finding.
>
> **Review status: same-model review.** Correctness, originality, and value were assessed by the same-model review, not an independent reviewer. Originality is only to the best of our knowledge.

## Claim

For `r>0`, write

`U_r(K) = max_mu ∫∫ |x-y|^r dmu(x)dmu(y)`

for probability measures `mu` on `K`, and `C_r(K)=U_r(K)^(1/r)=Cap_{-r}(K)`.

In the setting of Qiuling Fan's Conjecture 5.9, let

`B=e^(i phi)`, `C=e^(-i phi)`, `phi in (pi/2, 2pi/3]`,

and move

`A=e^(i psi)`, `0 <= psi <= 2pi-3phi`.

The source run proves that for every `r>=2`,

`psi -> U_r({A,B,C})`

is nondecreasing on this whole interval. Hence the capacity is also nondecreasing and is maximized at the right endpoint `psi=2pi-3phi`, where `AC=BC`. For `r>2`, the increase is strict on each nontrivial portion of the three-point-support branch with `psi>0`.

Thus Fan's Conjecture 5.9 is proved in the source run.

Fan states that Conjecture 5.6 for odd regular polygons follows from Conjecture 5.9 together with his proved symmetric Step 1 (Lemma 5.8) and the two-point reduction. Under those published ingredients, the source run therefore completes Fan's stated scheme for every odd `N>=3` and every `r>2`.

## Proof

Put

`a=(phi-psi)/2`, `b=(phi+psi)/2`.

Then `a+b=phi`, `b-a=psi`, and throughout the allowed interval

`0<a<=b<=pi-phi<=pi/2`.

The side lengths are

`x=AB=2 sin(a)`, `y=AC=2 sin(b)`, `c=BC=2 sin(phi)`,

with `x<=y<=c`. Set

`X=x^r`, `Y=y^r`, `Z=c^r`, `D=X+Y-Z`.

By the Clark--Laugesen three-point formula quoted as Fan's Lemma 5.7,

`U_r = Z/2` when `D<=0`,

and

`U_r = 2XYZ/(4XY-D^2)` when `D>0`.

So the energy is constant on the two-point-support branch. On the three-point branch define

`H=D^2/(XY)`.

Then

`U_r=2Z/(4-H)`,

so it suffices to show that `H` is nondecreasing.

Differentiating with respect to `psi` gives

`X'/X = -(r/2) cot(a)`,

`Y'/Y = (r/2) cot(b)`,

and

`D'=(r/2)(Y cot(b)-X cot(a))`.

Therefore

`(1/r) d(log H)/dpsi = (Y cot(b)-X cot(a))/D + (cot(a)-cot(b))/2`.

Multiplying by the positive quantity `2D sin(a) sin(b)` reduces its sign to the sign of

`(Y-X) sin(phi) - Z sin(psi)`.                                      (1)

Normalize

`u=sin(a)/sin(phi)`, `v=sin(b)/sin(phi)`.

Because `b<=pi-phi<=pi/2`, one has `0<u<=v<=1`. The three-point condition is

`u^r+v^r>1`.                                                        (2)

Also

`v^2-u^2 = (sin^2(b)-sin^2(a))/sin^2(phi) = sin(psi)/sin(phi)`.      (3)

After dividing (1) by the positive factor `sin^(r+1)(phi)`, it is enough to prove

`v^r-u^r >= v^2-u^2`.                                               (4)

### Power-difference lemma

If `r>=2`, `0<=u<=v<=1`, and `u^r+v^r>=1`, then

`v^r-u^r >= v^2-u^2`.

For `r=2` this is equality. Suppose `r>2`, put `q=r/2>1`, `s=u^2`, `t=v^2`, `alpha=1/q`, `A=s^q`, and `B=t^q`. Then

`0<=A<=B<=1`, `A+B>=1`,

and the target becomes

`B-A >= B^alpha-A^alpha`.                                          (5)

For fixed `A`, set

`Phi_A(B)=B-A-B^alpha+A^alpha`.

For `B>=1/2`,

`Phi_A'(B)=1-alpha B^(alpha-1)>=0`,

because `alpha 2^(1-alpha)<=1`.

If `A>=1/2`, then `B>=A`, so `Phi_A(B)>=Phi_A(A)=0`.

If `A<=1/2`, then `B>=1-A`, and

`Phi_A(B) >= 1-2A-(1-A)^alpha+A^alpha =: F(A)`.

Now `F(0)=F(1/2)=0`, while for `0<A<1/2`,

`F''(A)=alpha(alpha-1)[A^(alpha-2)-(1-A)^(alpha-2)]<0`.

Thus `F` is concave between two zero endpoints and hence `F(A)>=0`. This proves the lemma and therefore (4).

It follows that `H`, and hence `U_r`, is nondecreasing wherever `D>0`. At `D=0`, the three-point formula agrees continuously with the two-point value `Z/2`. Once a three-point branch has begun, its value is `>Z/2` and nondecreasing, so it cannot later return to a boundary point where the value would again be `Z/2`. Therefore the two-point branch, if present, is an initial constant interval followed by one terminal nondecreasing three-point branch.

Consequently `U_r` and `C_r` are globally nondecreasing in `psi`, proving the claimed endpoint maximum.

## Odd-polygon consequence

Fan's paper states that Conjecture 5.6 follows from Conjecture 5.9 and Lemma 5.8. Thus, subject to those published reductions, the source run establishes the odd-polygon energy formula

`U_r(P_N)=2^(r-1) sin^r(theta_N)/(1-2^(r-2) cos^r(theta_N))`,

where

`theta_N=(N-1)pi/(2N)`,

for every odd `N>=3` and `r>2`, with the equilibrium support and masses described in Fan's Conjecture 5.6.

## Computational corroboration

The compact verifier in `artifacts/verify.py` checks the scalar power-difference inequality on a dense grid, the derivative-sign reduction, monotonicity of the exact two-branch three-point energy on a deterministic grid, and 10,000 randomized triples. These computations are sanity checks only; the claim rests on the analytic argument above.

A compact proof note from the source run is archived as `artifacts/proof_note.md`.

## Closest prior work

- Qiuling Fan, *Riesz capacity ratios with negative exponents*, arXiv:2609.11186v1 (2026), is the direct parent source. The source run reports that public v1 explicitly labels the relevant Step 2 as unproved and states it as Conjecture 5.9.
- The exact three-point energy formula is due to Clark and Laugesen and is quoted as Fan's Lemma 5.7.
- The source run searched exact conjecture identifiers, the parent arXiv identifier, odd-polygon equilibrium terminology, three-point Riesz-capacity terminology, and stronger/equivalent formulations. It found no public proof or stronger theorem visibly implying Conjecture 5.9.

## Limitations

The parent preprint was only about one week old at the time of the source run, so an unposted author revision, private communication, or not-yet-indexed independent solution could duplicate the argument. The scalar power-difference inequality may itself be known in another guise; the source run did not locate an existing application that closes Fan's Step 2. No independent human, independent-agent, formal, or peer review is asserted.

The source run also records a scheduler limitation: a prior unrelated execution remained active for roughly the first 2 minutes 40 seconds of this run before that overlap became observable. The scheduler exposed no hard mutual-exclusion lock.
