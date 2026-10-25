# Independent mathematical audit

## correctness

PASS

Exact counterexample to Kiran Kumar--Upender Reddy Theorem 4.2 (2020): all coefficient spaces H_j=H=R^2, K=I has dense range; Lambda_1=[[1,0],[0,0]], Lambda_2=[[0,1],[0,0]], Lambda_j=0 for j>=3. Lambda_1^*Lambda_1+Lambda_2^*Lambda_2=I, so for every f the K-g-frame inequalities hold with A=B=1. T=T^*=diag(1,0) is a closed-range orthogonal projection and T Lambda_j=T^*Lambda_j=Lambda_j for all j. Both transformed systems remain Parseval, yet TT^*=T has kernel span(e_2) and is noninvertible. This is one complete finite-dimensional counterexample to the source’s universal theorem, not a finite-to-infinite extrapolation; the same matrices work over C^2 if the convention is complex Hilbert spaces. For any proper closed span M of the coefficient ranges, P_M postcomposition leaves every Lambda_j unchanged, exposing the missing coefficient-target visibility. The source proof makes an invalid global-kernel inference from lower bounds on Lambda_j^* T^*T Lambda_j: those bounds only test T on the coefficient ranges. For the stated supplementary sufficient repair in the ordinary g-frame case, if C_Lambda:H->oplus_j H is onto, g-frame bounded-below and onto imply C_Lambda is an isomorphism. Since C_(T Lambda)=D_T C_Lambda and C_(T^* Lambda)=D_(T^*) C_Lambda, both transformed lower bounds imply D_T and D_(T^*) bounded below. Testing one coordinate gives T and T^* bounded below; hence range(T) is closed and dense, so T is invertible. The sufficient repair is restricted to identically typed coefficient spaces and K=I.

## originality

PASS

The 2020 primary target actually states the false TT* invertibility conclusion; the exact projection counterexample and its mechanism are not in its Theorem 4.2 proof. The closest mathematical predecessor, Ramu--Johnson Theorem 3.7, treats transformed frame vectors and proves a valid invertibility theorem: its coefficients <f,T f_j>=<T^* f,f_j> test the entire ambient space. The corresponding operator-valued postcomposition T Lambda_j can act identically on all coefficient data while killing an unused target subspace, so the vector result does not imply the false theorem or already supply this theorem-specific counterexample. Four fresh Resultary semantic searches and targeted exact-title, DOI, theorem-number, erratum, range-projection web searches found only the audited identical published finding as an exact match; it is excluded as independent priority. Related published findings on right composition Lambda_j T, fusion-frame adjoint ranges, and closed-range compression have different order of composition and different target conclusions; their complete RESULT statements were read. This PASS is best-of-knowledge for the exact correction and coefficient-range mechanism, not a claim that projections or the frame inequality are new.

## value

PASS

This is a motivated correction to an explicit published operator-invertibility theorem used to justify extensions from vector K-frames to operator-valued K-g-frames. The exact 2x2 Parseval example satisfies the strongest benign cases K=I and closed-range self-adjoint T, avoiding ill-typed or delicate pathologies. The coefficient-range principle explains why the published inference loses information, rather than merely showing an isolated failed numerical estimate, and the onto-analysis sufficient condition exhibits one rigorous way to restore global invertibility. A user applying the source theorem needs exactly this obstruction/visibility condition; a theorem-specific conceptual correction can be worthwhile despite its elementary matrices. No broad universal repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
