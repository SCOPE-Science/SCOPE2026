# Independent mathematical audit

## correctness

PASS

Reassessed /workspace/repairs/5/RESULT.md. The frozen proof used (d+tr(s))/2 to recover an integer multiplicity from a characteristic-p trace; that gives only a congruence in general. Also, the frozen prose's nonconstant even-length coefficients have the m=1 exception (both equal q^k). The replacement explicitly treats that exception and uses exactness of positive eigenspaces on each invariant-filtration short exact sequence: (I+s)/2 lifts positives in the quotient to positives upstairs. Even layers contribute r, odd layers m−r, so their integer sum is km or km+r. The involution sJ acts identically on the graded layers; −sJ swaps signs, giving the second factor's stated dimension. The coefficient formula also checks: s determines t=s gε, and s=Aσ with σ(x)=(1+x)^(-1)−1, Aσ(A)=I. If A≡S+x^jD at a lifting layer, DS+(−1)^j SD=0, so conjugation by I−x^j DS/2 removes that coefficient. The stabilizer of Sσ has constant quotient GL_r×GL_(m−r); averaging gives surjectivity of each truncation of the fixed group, with fixed fibers of dimensions r²+(m−r)² in even degree and 2r(m−r) in odd degree. Dividing the centralizer order by that stabilizer and using the complementary-subspace count yields both exponents, including r=0,m with GL_0 trivial. Independent bounded checks over F_3 via truncated lifts and standard matrices recovered (81,108,81) at n=m=2 and (81,972,81) at n=3,m=2, including the reversed second-factor rank list (4,3,2) for the odd negative product. These are bounded checks, not an extension-field or all-dimension certificate; the general verification is the proof in the replacement. Frozen checker.py was inspected and not executed.

## originality

PASS

After repair the contribution remains the evaluated pointwise counts by residual rank for homogeneous signed-unipotent products. Existence, prescribed-product orbit structure and supported pairs of ordinary ranks are credited to prior work. No known exact size evaluation for these fibers was established in the inspected material.

## value

PASS

The repaired claim supplies the number of ordered decompositions in each residual stratum at a fixed target, a natural finite-field refinement of existence and orbit classification. For even block size all ordinary factor ranks coincide, so an ordinary rank table cannot recover the residual population; the alternating stabilizer dimensions give a concrete reason for the parity-dependent counts. Only the stratum sizes and their enumerator are the quantitative increment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
