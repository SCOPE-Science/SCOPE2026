# Independent mathematical audit

## correctness

PASS

The binary word has a unique triple (a,b,c) of zero-run lengths before, between and after its two ones, and the ordinary scattered 01 count is x=2a+b. The least rotation starts at a longest of the two circular zero runs b,N−b, including ties and the empty-run case, so its 01 count is y=N+max(b,N−b). Thus at most two b values are possible, and each fixes a,c. When N is odd the candidates differ in parity, and exactly one can have x−b even in a nonempty fiber. For N=2h, distinct gaps must be t and 2h−t with t<h. Taking the longer middle gap and exterior lengths j,t−j fixes x=2j+2h−t; the shorter middle gap then forces exterior lengths j+h−t,h−j, both nonnegative for 0≤j≤t. The long-gap word uniquely recovers t,j. The doubletons therefore number Σ_{t=0}^{h−1}(t+1)=h(h+1)/2; subtracting twice this from binom(2h+2,2) gives (h+1)² singleton fibers and adding both fiber counts gives (h+1)(3h+2)/2 observations. This also handles N=0, and one representative per fiber is necessary and sufficient for a maximum zero-error code. The uniquely recoverable proportion counts singleton words relative to all inputs. No finite computation is needed for exhaustiveness. The frozen direct-rotation checker and its recorded N=0..60 run were inspected, not executed.

## originality

PASS

The credited result is the full joint-fiber spectrum and collision parametrization in the all-N two-one family, not the joint observation or the existence of an unresolved collision. Dick et al. (LATA 2020) Example 8 contains one exact doubleton from the theorem and their full text classifies whether an entire ordinary class can be split by its L-Parikh observation. That yes/no classification does not enumerate the surviving fibers inside classes it can split. In particular at N=6 and x=6 the ordinary class is split into two distinct doubletons, not resolved into singleton words. The indexed alternatives inspected concern other matrices or objectives. The 2021 journal version and 2022 toolkit remain explicit access risks, not grounds to infer absence or reject a verified distinct result.

## value

PASS

The established joint observation motivates the least nontrivial two-marker slice; even there, detecting a split of an ordinary class does not determine actual recovery. The theorem gives a decoder with at most two candidates, resolves all residual collisions, and quantifies the odd/even difference for unique recovery and optimal zero-error code size. This exact all-content spectrum answers a natural ambiguity question left open by class-level distinguishability and is not a re-enumeration of the known example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
