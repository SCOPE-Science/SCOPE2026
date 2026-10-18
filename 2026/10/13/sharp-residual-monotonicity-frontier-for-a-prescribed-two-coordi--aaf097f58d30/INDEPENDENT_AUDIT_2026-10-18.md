# Independent mathematical audit

## correctness

PASS

For A=[[a,c],[c,b]] SPD, the exact coordinate-1 then coordinate-2 residual update is r^+=(-c/b*(r_2−(c/a)r_1),0), with induced Euclidean norm |c|/b*sqrt(1+c²/a²). Normalizing eigenvalues to 1,kappa and u=tan²(rotation angle) yields the displayed rational Phi_kappa(u). Descartes sign analysis of the derivative quartic gives one positive stationary maximum for every kappa>1; boundary Phi(0)=Phi(infinity)=0. Independently used exact SymPy resultant elimination for Phi=1 and dPhi/du=0, reproducing precisely −kappa^6(kappa−1)^20(kappa²+kappa+1)P(kappa), where P=32kappa^6−131kappa^5−144kappa^4−362kappa^3−144kappa²−131kappa+32. Root isolation gives the unique >1 frontier kappa*=5.36076789614546. A=[[5,2],[2,2]] has eigenvalues 1,6 and maps residual (2,−5) to (29/5,0), proving expansion past the boundary. Continuity and uniqueness of tangency establish the iff statement, not numerical sampling alone.

## originality

PASS

Prior Resultary work completely classifies 2x2 Gauss–Seidel one-sweep Euclidean SOLUTION-ERROR amplification under choice of the better coordinate ordering, threshold about 8.35241. The audited theorem fixes an arbitrary prescribed order and measures the Euclidean RESIDUAL norm r=Ae, giving a mathematically distinct optimization and sharp frontier 5.36077. General randomized coordinate descent sources supply update formulas, not this residual amplification threshold.

## value

PASS

The exact condition-number frontier resolves a classical practical distinction: Gauss–Seidel is objective/energy decreasing on SPD matrices while its Euclidean residual can initially increase. The sharp 2D boundary and exact counterexample diagnose when residual-based stopping monitors need not be sweep-monotone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
