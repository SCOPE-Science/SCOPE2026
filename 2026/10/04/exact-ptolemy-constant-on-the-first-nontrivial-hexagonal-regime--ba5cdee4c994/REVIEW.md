# Independent mathematical audit

## correctness

PASS

Let \(H_\gamma(x,y)=\sqrt{x^2+(1-\gamma^2)y^2}\). The six vertices of the \(N_\gamma\)-unit ball lie on the \(H_\gamma\)-unit ellipse, so convexity gives \(H_\gamma\le N_\gamma\). Weighted Cauchy gives \(|x|+(1-\gamma)|y|\le\sqrt{2/(1+\gamma)}H_\gamma\), and for \(0<\gamma<1/2\) this factor also dominates the axis branch \(|y|\). Hence \(N_\gamma\le\sqrt{2/(1+\gamma)}H_\gamma\), and Hilbert-space Ptolemy yields \(C_{\mathrm{Pt}}\le2/(1+\gamma)\). The explicit triple \(x=(-1,0)\), \(y=(\gamma,1)\), \(z=(-(1+\gamma),1)\) has the six required norms \(2,2,1,1,1,1+2\gamma\), giving ratio \(2/(1+\gamma)\). A fresh symbolic replay independently reproduced this ratio.

## originality

PASS

The defining Chica-Merí paper studies the same one-parameter hexagonal family but computes its rank-one numerical index, not its Ptolemy constant. The 2010 Ptolemy paper computes several individual spaces, including a fixed hexagon example, while Zuo's 2012 general absolute-norm criteria do not directly determine this crossing regime. A related published SCOPE record gives the Euclidean Banach-Mazur profile \(\sqrt{2/(1+\gamma)}\) on this regime, which supplies the same natural upper comparison but not the matching Ptolemy witness or equality. No distinct exact full-interval Ptolemy theorem was located in the bounded searches.

## value

PASS

The Ptolemy constant is a standard quantitative inner-product defect. The family is a classical explicit hexagonal deformation, and the theorem gives the exact first nontrivial parameter regime with a sharp equality mechanism between Euclidean distortion and a concrete Ptolemy witness. This is a motivated geometric boundary calculation rather than an arbitrary numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
