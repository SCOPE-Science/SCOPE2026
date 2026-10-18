# Independent mathematical audit

## correctness

PASS

For F(x,y)=(y,ay−y³−bx), a≥0 and 0<b<1, all prime two cycles have coordinates (u,v)<->(v,u) satisfying B u=av−v³ and B v=au−u³, B=1+b. Factoring sum/difference gives either u=−v with u²=a+B (one antipodal saddle), u=v (fixed, excluded), or uv=B and u²+v²=a (exactly two sign-reversed non-antipodal cycles for a>2B). The return determinant is b²; trace for non-antipodal is −2a²+9B²−2b. Exact Jury inequalities give both sinks for 2B<a<sqrt((9B²+(1−b)²)/2), multipliers −1,−b² at equality, saddles above. Antipodal trace (−2a−3B)²−2b exceeds 1+b² for all specified parameters. Independent symbolic trace/threshold computations and sampled verifier review agree. The theorem is exhaustive for real prime-two orbits only, not other periods or nonlinear behavior at the flip.

## originality

PASS

Coomes–Koçak–Palmer 2026 Example 3.2 studies precisely F(y,ay−y³−bx), quotes a=2(1+b) cycle birth and numerical attracting windows at b=.2, but does not give this two-parameter complete count and exact flip threshold. Crucial close predecessor Chen–Wang–Li 2017 primary full PDF was obtained in this run and materially read: its printed equation (3) uses F(x,y)=(y,a x−x³−b y), NOT the submitted constant-determinant map. Its Jacobian determinant is state-dependent whereas current model det DF=b, hence its fixed-point Flip/Hopf criteria cannot cover the claim by parameter renaming. No located stronger same-formula result supplies the count and exact threshold. Originality remains best-of-knowledge, allowing alternate map conventions and older chaos literature as risks.

## value

PASS

The exact global prime-two orbit count and two-parameter sharp sink-to-saddle transition improve numerical bifurcation reports for a classical cubic planar map. This is a natural complete low-period classification, not a mere fixed-point stability restatement. The endpoint double-multiplier factorization and b=.2 constant sqrt(34/5) distinguish spectral onset from basin/global chaos claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
