# Independent mathematical audit

## correctness

PASS

The source formula factors into B=Nβ1Λ/(cd)+β2Λ/(δ_I d)=508/23 and delay fraction α/(α+δ_L)=5/7. Under m1=m2=1,τ1=τ2=τ, this gives (508/23)(1−2ξ/7)e^(−τ). With ξ=.001, prefactor 444373/20125 and τ crossing log(prefactor)=3.0947014765; at .5 and 1.75 both R0>1. At τ=1.75, ξ=.05 and .025 give exact prefactors 762/35 and 17653/805; derivative wrt ξ is −1016/161 e^(−7/4)<0. For all ξ∈[0,1], R0≥(2540/161)e^(−7/4)>2.74. Independently recomputed all rational prefactors and numerical values; source verify.py actual blob also inspected. Calculations concern published formula/table/captions, not hidden simulation code.

## originality

PASS

The delayed-HIV threshold formula and delay-survival mechanism are established, so they are explicitly not claimed as new. The exact source-specific numerical contradiction, its sign reversal, and disappearance of both advertised R0=1 crossings were not found in the initiating article or searched corrigenda.

## value

PASS

Both figures are used as evidence for crossing a biologically meaningful epidemic threshold; exact printed parameters keep every illustrated case supercritical and reverse the stated latency effect. This materially changes interpretation of the published numerical validation and is not a negligible rounding difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
