# Independent mathematical audit

## correctness

PASS

At the disease-free equilibrium the eight infected/latent coordinates (EC,EM,ECM,IC,IM,ICM,Er,Ir) decouple from stable noninfected compartments at linear order. The nonnegative new-infection matrix F has F14=F16=βa,F25=F26=βc,F28=βb,F78=βr; V is lower triangular with positive diagonal (a,b,c,d,e,u,g,h), and off-diagonal transfers ECM<-φC EC, ECM<-φM EM, IC<-θC EC, IM<-θM EM, ICM<-θCM ECM, Ir<-θr Er. Exact inversion reduces FV^-1 nonzero eigenvalues to 3x3 G=[[A,B,0],[C,D,βb θr/(gh)],[0,0,βr θr/(gh)]] with w=θCM/(cu), A=βa(θC/d+φC w)/a, B=βa φM w/b, C=βc φC w/a, D=βc(θM/e+φM w)/b. Perron eigenvalue of coupled human 2x2 is (A+D+sqrt((A-D)^2+4BC))/2; max with rodent value gives exact strict local DFE threshold by nonsingular-M-matrix NGM theorem. Every parameter in the exhibited rational witness is positive and G evaluates exactly [[329/180,56/45,0],[8/45,47/180,1/4],[0,0,1/4]], human threshold 47/45+sqrt(27049)/180>1 while source separate Rc=7/8,Rm=1/8,Rr=1/4. Independently rebuilt F,V symbolically, checked all matrix entries and exact witness. Equality Rfull=1 and global dynamics explicitly excluded.

## originality

PASS

Acheneje et al (2025), the same 15-class COVID–Mpox source, print cross-progression paths φC EC+φM EM into co-exposure and simultaneous infectivity from ICM, yet compute separate-disease reproduction ratios and assert the maximum as the full threshold. Standard Diekmann and van den Driessche methods give a general construction but not its model-specific coupled 2x2 Perron block or the strictly positive contradiction. Resultary has a qualitatively analogous shared-exposed coupled-threshold failure for a different multistrain model; it is not this matrix. The exact published-model correction is a substantive new statement best-of-knowledge.

## value

PASS

An open set of all-positive parameters flips the local DFE stability verdict from the paper’s reported subcritical maximum to a supercritical coupled Perron root. This is a substantive correctness correction to a fifteen-compartment epidemiological model and explains exactly which latent co-infection pathways cause the failure; not a textbook reapplication without a model-specific consequence. The claim carefully excludes public-health predictions and does not infer nonlinear endemic prevalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
